db.users.insertMany([
  { user_id: 1, name: "Arun", email: "arun@gmail.com", country: "India" },
  { user_id: 2, name: "Divya", email: "divya@gmail.com", country: "India" },
  { user_id: 3, name: "Karthik", email: "karthik@gmail.com", country: "Malaysia" },
  { user_id: 4, name: "Priya", email: "priya@gmail.com", country: "Singapore" },
  { user_id: 5, name: "Vignesh", email: "vignesh@gmail.com", country: "India" }
]);

db.movies.insertMany([
  { movie_id: 101, title: "Vikram", genre: "Action", release_year: 2022, duration: 175 },
  { movie_id: 102, title: "96", genre: "Romance", release_year: 2018, duration: 158 },
  { movie_id: 103, title: "Soorarai Pottru", genre: "Drama", release_year: 2020, duration: 153 },
  { movie_id: 104, title: "Super Deluxe", genre: "Thriller", release_year: 2019, duration: 176 },
  { movie_id: 105, title: "Jigarthanda", genre: "Crime", release_year: 2014, duration: 171 },
  { movie_id: 106, title: "Ratsasan", genre: "Psychological Thriller", release_year: 2018, duration: 170 }
]);

db.watch_history.insertMany([
  { watch_id: 1, user_id: 1, movie_id: 101, watched_on: new Date("2024-01-10"), watch_time: 160 },
  { watch_id: 2, user_id: 2, movie_id: 102, watched_on: new Date("2024-02-15"), watch_time: 158 },
  { watch_id: 3, user_id: 1, movie_id: 103, watched_on: new Date("2024-03-20"), watch_time: 150 },
  { watch_id: 4, user_id: 3, movie_id: 101, watched_on: new Date("2024-04-12"), watch_time: 175 },
  { watch_id: 5, user_id: 4, movie_id: 104, watched_on: new Date("2024-05-01"), watch_time: 153 },
  { watch_id: 6, user_id: 5, movie_id: 105, watched_on: new Date("2024-06-08"), watch_time: 100 },
  { watch_id: 7, user_id: 5, movie_id: 106, watched_on: new Date("2024-07-03"), watch_time: 170 },
  { watch_id: 8, user_id: 5, movie_id: 105, watched_on: new Date("2024-07-10"), watch_time: 160 }
]);

 Basic:
 // 1. Find all movies with duration > 100 minutes.
db.movies.find({duration:{$gt:100}})

 // 2. List users from 'India'.
db.users.find({country:"India"})

 // 3. Get all movies released after 2020.
db.movies.find({release_year:{$gt:2020}})

 Intermediate:
 // 4. Show full watch history: user name, movie title, watch time.
db.watch_history.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "user_id",
      foreignField: "user_id",
      as: "user"
    }
  },
  {
    $lookup: {
      from: "movies",
      localField: "movie_id",
      foreignField: "movie_id",
      as: "movie"
    }
  },
  {
    $project: {
      _id: 0,
      user_name: { $arrayElemAt: ["$user.name", 0] },
      movie_title: { $arrayElemAt: ["$movie.title", 0] },
      watch_time: 1
    }
  }
]);


 // 5. List each genre and number of times movies in that genre were watched.
db.watch_history.aggregate([
  {
    $lookup: {
      from: "movies",
      localField: "movie_id",
      foreignField: "movie_id",
      as: "movie"
    }
  },
  { $unwind: "$movie" },
  {
    $group: {
      _id: "$movie.genre",
      times_watched: { $sum: 1 }
    }
  }
]);

 // 6. Display total watch time per user.
db.watch_history.aggregate([
  {
    $group: {
      _id: "$user_id",
      total_watch_time: { $sum: "$watch_time" }
    }
  },
  {
    $lookup: {
      from: "users",
      localField: "_id",
      foreignField: "user_id",
      as: "user"
    }
  },
  {
    $project: {
      user_name: { $arrayElemAt: ["$user.name", 0] },
      total_watch_time: 1
    }
  }
]);

 Advanced:
 // 7. Find which movie has been watched the most (by count).
db.watch_history.aggregate([
  {
    $group: {
      _id: "$movie_id",
      watch_count: { $sum: 1 }
    }
  },
  {
    $lookup: {
      from: "movies",
      localField: "_id",
      foreignField: "movie_id",
      as: "movie"
    }
  },
  { $unwind: "$movie" },
  {
    $project: {
      movie_title: "$movie.title",
      watch_count: 1
    }
  },
  { $sort: { watch_count: -1 } },
  { $limit: 1 }
]);

 // 8. Identify users who have watched more than 2 movies.
db.watch_history.aggregate([
  {
    $group: {
      _id: "$user_id",
      unique_movies: { $addToSet: "$movie_id" }
    }
  },
  {
    $project: {
      movie_count: { $size: "$unique_movies" }
    }
  },
  { $match: { movie_count: { $gt: 1 } } },
  {
    $lookup: {
      from: "users",
      localField: "_id",
      foreignField: "user_id",
      as: "user"
    }
  },
  {
    $project: {
      user_name: { $arrayElemAt: ["$user.name", 0] },
      movie_count: 1
    }
  }
]);

 // 9. Show users who watched the same movie more than once.
db.watch_history.aggregate([
  {
    $group: {
      _id: { user_id: "$user_id", movie_id: "$movie_id" },
      count: { $sum: 1 }
    }
  },
  { $match: { count: { $gt: 1 } } },
  {
    $lookup: {
      from: "users",
      localField: "_id.user_id",
      foreignField: "user_id",
      as: "user"
    }
  },
  {
    $lookup: {
      from: "movies",
      localField: "_id.movie_id",
      foreignField: "movie_id",
      as: "movie"
    }
  },
  {
    $project: {
      user_name: { $arrayElemAt: ["$user.name", 0] },
      movie_title: { $arrayElemAt: ["$movie.title", 0] },
      count: 1
    }
  }
]);

 // 10. Calculate percentage of each movie watched compared to its full duration ( watch_time/duration * 100 )
db.watch_history.aggregate([
  {
    $lookup: {
      from: "movies",
      localField: "movie_id",
      foreignField: "movie_id",
      as: "movie"
    }
  },
  { $unwind: "$movie" },
  {
    $project: {
      user_id: 1,
      movie_title: "$movie.title",
      percentage_watched: {
        $round: [
          { $multiply: [{ $divide: ["$watch_time", "$movie.duration"] }, 100] },2]}}}]);