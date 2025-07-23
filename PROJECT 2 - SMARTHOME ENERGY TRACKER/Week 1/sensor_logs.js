// sensor logs
db.sensor_logs.insertMany([
  {
    device_id: 101,
    timestamp: ISODate("2025-07-20T09:00:00Z"),
    power_watt: 1500,
    status: "ON"
  },
  {
    device_id: 102,
    timestamp: ISODate("2025-07-20T12:00:00Z"),
    power_watt: 200,
    status: "ON"
  },
  {
    device_id: 104,
    timestamp: ISODate("2025-07-20T07:00:00Z"),
    power_watt: 1800,
    status: "ON"
  }
]);

// indexing
db.sensor_logs.createIndex({ device_id: 1 });
db.sensor_logs.createIndex({ timestamp: 1 });
