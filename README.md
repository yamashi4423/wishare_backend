# wishare_backend

wishare のバックエンド

### 使用技術

- Django
- Cloud Run

### ワークフロー

#### github と連携しない場合

1.  docker イメージを作成

```bash
   docker build -t [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE]:[TAG] .
```

2.  docker イメージを Artifact Registry に push

```bash
   docker push [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE]:[TAG]
```

3.  Cloud Run にデプロイ

```bash
gcloud run deploy --image [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE]:[TAG] --platform=managed --project=[PROJECT_ID]
```

#### github と連携する場合

後程
