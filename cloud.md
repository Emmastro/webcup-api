

PROJECT_ID=$(gcloud config get-value core/project)

REGION=us-central1

gcloud iam service-accounts create cloudrun-serviceaccount

SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter cloudrun-serviceaccount --format "value(email)")

gcloud sql instances create webcup-db --project $PROJECT_ID --database-version POSTGRES_13 --tier db-f1-micro --region $REGION

gcloud sql databases create webcup_test --instance webcup-db

DJPASS="$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 30 | head -n 1)"
gcloud sql users create djuser --instance webcup-db --password $DJPASS


PROJECT_ID=$(gcloud config get-value core/project)

REGION=us-central1

gcloud iam service-accounts create cloudrun-serviceaccount

SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter cloudrun-serviceaccount --format "value(email)")

gcloud sql instances create webcup-db --project $PROJECT_ID --database-version POSTGRES_13 --tier db-f1-micro --region $REGION

gcloud sql databases create webcup_test --instance webcup-db

DJPASS="$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 30 | head -n 1)"
gcloud sql users create djuser --instance webcup-db --password $DJPASS



gcloud secrets versions list application_settings

mv webcup/settings.py webcup/basesettings.py


export PROJECTNUM=$(gcloud projects describe ${PROJECT_ID} --format 'value(projectNumber)')
export CLOUDBUILD=${PROJECTNUM}@cloudbuild.gserviceaccount.com

gcloud secrets add-iam-policy-binding application_settings \
  --member serviceAccount:${CLOUDBUILD} --role roles/secretmanager.secretAccessor

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member serviceAccount:${CLOUDBUILD} --role roles/cloudsql.client

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member serviceAccount:${CLOUDBUILD} --role roles/storage.objects.get


mkdir webcup/migrations
touch webcup/migrations/__init__.py
touch webcup/migrations/0001_createsuperuser.py


export PROJECTNUM=$(gcloud projects describe ${PROJECT_ID} --format 'value(projectNumber)')
export CLOUDBUILD=${PROJECTNUM}@cloudbuild.gserviceaccount.com

gcloud secrets add-iam-policy-binding application_settings \
  --member serviceAccount:${CLOUDBUILD} --role roles/secretmanager.secretAccessor

# submit docker file

gcloud builds submit --pack image=gcr.io/${PROJECT_ID}/webcup-image
gcloud builds submit --config migrate.yaml
gcloud run deploy django-cloudrun \
  --platform managed \
  --region $REGION \
  --image gcr.io/${PROJECT_ID}/webcup-image \
  --set-cloudsql-instances ${PROJECT_ID}:${REGION}:webcup-db \
  --set-secrets APPLICATION_SETTINGS=application_settings:latest \
  --service-account $SERVICE_ACCOUNT \
  --allow-unauthenticated



gcloud builds submit --pack image=gcr.io/${PROJECT_ID}/webcup-image
gcloud run services update django-cloudrun \
  --platform managed \
  --region $REGION \
  --image gcr.io/${PROJECT_ID}/webcup-image