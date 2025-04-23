#!/bin/bash

BACKUP_DIR="/Users/talha/mongo-backups"

MONGO_REMOTE_URI="mongodb://developer:developer@192.168.200.64:27017"
MONGO_LOCAL_URI="mongodb://developer:developer@localhost:27017"

DATABASES=(
    NESY_ArasDxDev_EmailDB
    NESY_ArasDxDev_EurodisDB
    NESY_ArasDxDev_EventTowerDB
    NESY_ArasDxDev_CacheDB
    NESY_ArasDxDev_CustomerDB
    NESY_ArasDxDev_GeocodeDB
    NESY_ArasDxDev_HistoryDB
    NESY_ArasDxDev_HubCompanionDB
    NESY_ArasDxDev_IntegrationDB
    NESY_ArasDxDev_NotificationDB
    NESY_ArasDxDev_ParcelShop_InventoryDB
    NESY_ArasDxDev_PushNotificationDB
    NESY_ArasDxDev_ShipmentDB
    NESY_ArasDxDev_SmsDB
    NESY_ArasDxDev_TaskDB
    NESY_ArasDxDev_TrackingDB
    NESY_ArasDxDev_UserDB
    NESY_ArasDxDev_VersionDB
    NESY_ArasDxDev_ViberDB
)

echo "Başlıyor: MongoDB veritabanları taşınıyor..."

for db in "${DATABASES[@]}"
do
  NEW_NAME="${db/NESY_ArasDxDev_/NESY_}"

  echo "Yedekleniyor: $db"
  mongodump --uri="${MONGO_REMOTE_URI}/${db}" --authenticationDatabase=admin --out="${BACKUP_DIR}/${db}"

  echo "Geri yükleniyor: ${NEW_NAME}"
  mongorestore --uri="${MONGO_LOCAL_URI}" --authenticationDatabase=admin \
    --nsFrom="${db}.*" --nsTo="${NEW_NAME}.*" \
    --dir="${BACKUP_DIR}/${db}"

done

echo "✅ Tüm veritabanları başarıyla taşındı ve isimleri değiştirildi!"
