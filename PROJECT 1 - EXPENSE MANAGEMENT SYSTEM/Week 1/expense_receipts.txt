db.receipts.insertMany([
  {
    user_id: 1,
    receipt_id: "R001",
    note: "Weekly groceries bill",
    receipt_date: new Date("2025-07-01"),
    amount: 2500.00
  },
  {
    user_id: 2,
    receipt_id: "R002",
    note: "House rent receipt",
    receipt_date: new Date("2025-07-01"),
    amount: 10000.00
  },
  {
    user_id: 3,
    receipt_id: "R003",
    note: "Dinner with friends",
    receipt_date: new Date("2025-07-02"),
    amount: 1200.00
  },
  {
    user_id: 4,
    receipt_id: "R004",
    note: "Electricity and water bill",
    receipt_date: new Date("2025-07-03"),
    amount: 1800.00
  },
  {
    user_id: 5,
    receipt_id: "R005",
    note: "Health checkup receipt",
    receipt_date: new Date("2025-07-04"),
    amount: 2200.00
  },
  {
    user_id: 6,
    receipt_id: "R006",
    note: "Transport expenses",
    receipt_date: new Date("2025-07-04"),
    amount: 800.00
  },
  {
    user_id: 7,
    receipt_id: "R007",
    note: "Tuition fees receipt",
    receipt_date: new Date("2025-07-05"),
    amount: 5000.00
  },
  {
    user_id: 8,
    receipt_id: "R008",
    note: "Entertainment expense",
    receipt_date: new Date("2025-07-05"),
    amount: 950.00
  },
  {
    user_id: 1,
    receipt_id: "R009",
    note: "Lunch outing",
    receipt_date: new Date("2025-07-06"),
    amount: 700.00
  },
  {
    user_id: 2,
    receipt_id: "R010",
    note: "Vegetable shopping",
    receipt_date: new Date("2025-07-07"),
    amount: 3000.00
  }
])

// indexing

db.receipts.createIndex({ user_id: 1 })
db.receipts.createIndex({ receipt_id: 1 }, { unique: true })