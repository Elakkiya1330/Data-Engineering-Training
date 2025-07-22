// 1. create or switch to the database
use bookstoreDB

// 2. Insert 5 books
db.books.insertMany([
  {
    book_id: 1,
    title: "The White Tiger",
    author: "Aravind Adiga",
    genre: "Fiction",
    price: 550,
    stock: 40
  },
  {
    book_id: 2,
    title: "Wings of Fire",
    author: "A.P.J. Abdul Kalam",
    genre: "Autobiography",
    price: 300,
    stock: 35
  },
  {
    book_id: 3,
    title: "Train to Pakistan",
    author: "Khushwant Singh",
    genre: "Historical Fiction",
    price: 280,
    stock: 20
  },
  {
    book_id: 4,
    title: "The Palace of Illusions",
    author: "Chitra Banerjee Divakaruni",
    genre: "Mythology",
    price: 320,
    stock: 25
  },
  {
    book_id: 5,
    title: "Interpreter of Maladies",
    author: "Jhumpa Lahiri",
    genre: "Short Stories",
    price: 250,
    stock: 30
  }
])

// 3. Insert 5 customers
db.customers.insertMany([
  {
    customer_id: 1,
    name: "Harish Kumar",
    email: "harish.kumar@gmail.com",
    city: "Chennai"
  },
  {
    customer_id: 2,
    name: "Surya Narayanan",
    email: "surya.narayanan@gmail.com",
    city: "Coimbatore"
  },
  {
    customer_id: 3,
    name: "Aadhithyan",
    email: "aadhithyan@gmail.com",
    city: "Madurai"
  },
  {
    customer_id: 4,
    name: "Nisha tharun",
    email: "nisha@gmail.com",
    city: "Hyderabad"
  },
  {
    customer_id: 5,
    name: "Rohan beno",
    email: "rohan@gmail.com",
    city: "Ahmedabad"
  }
])

// 4. Insert 7 orders
db.orders.insertMany([
  {
    order_id: 101,
    customer_id: 1,
    book_id: 2,
    order_date: new ISODate("2025-07-15T10:30:00Z"),
    quantity: 1
  },
  {
    order_id: 102,
    customer_id: 2,
    book_id: 1,
    order_date: new ISODate("2025-07-16T11:00:00Z"),
    quantity: 2
  },
  {
    order_id: 103,
    customer_id: 3,
    book_id: 5,
    order_date: new ISODate("2025-07-17T12:45:00Z"),
    quantity: 1
  },
  {
    order_id: 104,
    customer_id: 4,
    book_id: 3,
    order_date: new ISODate("2025-07-18T09:20:00Z"),
    quantity: 3
  },
  {
    order_id: 105,
    customer_id: 5,
    book_id: 4,
    order_date: new ISODate("2025-07-19T14:10:00Z"),
    quantity: 1
  },
  {
    order_id: 106,
    customer_id: 1,
    book_id: 1,
    order_date: new ISODate("2025-07-20T16:00:00Z"),
    quantity: 1
  },
  {
    order_id: 107,
    customer_id: 2,
    book_id: 5,
    order_date: new ISODate("2025-07-21T08:45:00Z"),
    quantity: 2
  }
])

 // PART 3: Write Queries
 // Basic Queries:
 // 1. List all books priced above 500.
db.books.find({ price: { $gt: 500 } })

 // 2. Show all customers from ‘Hyderabad’.
db.customers.find({ city: "Hyderabad" })

 // 3. Find all orders placed after January 1, 2023.
db.orders.find({ order_date: { $gt: new ISODate("2023-01-01") } })

Joins via $lookup :
 // 4. Display order details with customer name and book title.
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "customer"
    }
  },
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  {
    $project: {
      order_id: 1,
      order_date: 1,
      quantity: 1,
      customer_name: { $arrayElemAt: ["$customer.name", 0] },
      book_title: { $arrayElemAt: ["$book.title", 0] }
    }
  }
])


 // 5. Show total quantity ordered for each book.
db.orders.aggregate([
  {
    $group: {
      _id: "$book_id",
      total_quantity: { $sum: "$quantity" }
    }
  },
  {
    $lookup: {
      from: "books",
      localField: "_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  {
    $project: {
      book_title: { $arrayElemAt: ["$book.title", 0] },
      total_quantity: 1
    }
  }
])

 // 6. Show the total number of orders placed by each customer.
db.orders.aggregate([
  {
    $group: {
      _id: "$customer_id",
      total_quantity: { $sum: 1 }
    }
  },
  {
    $lookup: {
      from: "customers",
      localField: "_id",
      foreignField: "customer_id",
      as: "customer"
    }
  },
  {
    $project: {
      customer_name: { $arrayElemAt: ["$customer.name", 0] },
      total_quantity: 1
    }
  }
])

 // Aggregation Queries:
 // 7. Calculate total revenue generated per book.
db.orders.aggregate([
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  { $unwind: "$book" },
  {
    $group: {
      _id: "$book_id",
      book_title: { $first: "$book.title" },
      total_revenue: { $sum: { $multiply: ["$quantity", "$book.price"] } }
    }
  },
  {
    $project: {
      _id: 0,
      book_title: 1,
      total_revenue: 1
    }
  }
])

 // 8. Find the book with the highest total revenue.
db.orders.aggregate([
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  { $unwind: "$book" },
  {
    $group: {
      _id: "$book_id",
      book_title: { $first: "$book.title" },
      total_revenue: { $sum: { $multiply: ["$quantity", "$book.price"] } }
    }
  },
  { $sort: { total_revenue: -1 } },
  { $limit: 1 },
  {
    $project: {
      _id: 0,
      book_title: 1,
      total_revenue: 1
    }
  }
])

 // 9. List genres and total books sold in each genre.
db.orders.aggregate([
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  { $unwind: "$book" },
  {
    $group: {
      _id: "$book.genre",
      total_books_sold: { $sum: "$quantity" }
    }
  },
  {
    $project: {
      _id: 0,
      genre: "$_id",
      total_books_sold: 1
    }
  }
])

 // 10. Show customers who ordered more than 2 different books
db.orders.aggregate([
  {
    $group: {
      _id: { customer_id: "$customer_id", book_id: "$book_id" }
    }
  },
  {
    $group: {
      _id: "$_id.customer_id",
      unique_books_count: { $sum: 1 }
    }
  },
  {
    $match: {
      unique_books_count: { $gt: 1 }
    }
  },
  {
    $lookup: {
      from: "customers",
      localField: "_id",
      foreignField: "customer_id",
      as: "customer"
    }
  },
  {
    $project: {
      _id: 0,
      customer_name: { $arrayElemAt: ["$customer.name", 0] },
      unique_books_count: 1
    }
  }
])
