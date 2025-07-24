// MongoDB Assignment: Design & Query Challenge
 // Part 1: Create Collections and Insert Your Own Data
 // Create a small MongoDB database for a Job Portal. Design at least 3 collections with at least 5 documents each.
 // You are free to choose the fields, but you must include the following:
 // Suggested Collections (you can rename or adjust):
 // 1. jobs – job title, company, location, salary, job_type (remote/hybrid/on-site),posted_on

db.jobs.insertMany([
{ job_id:1, title:"Software Engineer", company:"Hexaware", location:"Bangalore", salary:900000, job_type:"remote", posted_on:new Date("2025-07-01") },
{ job_id:2, title:"Data Analyst", company:"TCS", location:"Hyderabad", salary:750000, job_type:"hybrid", posted_on:new Date("2025-07-05") },
{ job_id:3, title:"Product Manager", company:"Cognizant", location:"Delhi", salary:1200000, job_type:"on-site", posted_on:new Date("2025-07-08") },
{ job_id:4, title:"UX Designer", company:"Wipro", location:"Mumbai", salary:800000, job_type:"remote", posted_on:new Date("2025-07-10") },
{ job_id:5, title:"DevOps Engineer", company:"Amazon", location:"Chennai", salary:950000, job_type:"hybrid", posted_on:new Date("2025-07-12"),{ job_id:6, title:"Backend Developer", company:"Hexaware", location:"Bangalore", salary:1100000, job_type:"remote", posted_on:new Date("2025-07-14") },
  { job_id:7, title:"QA Engineer", company:"Hexaware", location:"Bangalore", salary:700000, job_type:"hybrid", posted_on:new Date("2025-07-15") },
  { job_id:8, title:"Data Scientist", company:"TCS", location:"Hyderabad", salary:1300000, job_type:"remote", posted_on:new Date("2025-07-16") } }
])

 // 2. applicants – name, skills, experience, city, applied_on

db.applicants.insertMany([
{ applicant_id:101, name:"Elakkiya", skills:["Python","MongoDB"], experience:3, city:"Mumbai", applied_on:new Date("2025-07-15") },
{ applicant_id:102, name:"Kashifa", skills:["SQL","PowerBI"], experience:2, city:"Delhi", applied_on:new Date("2025-07-16") },
{ applicant_id:103, name:"Varshini", skills:["Java","Spring Boot"], experience:4, city:"Chennai", applied_on:new Date("2025-07-17") },
{ applicant_id:104, name:"Lavanya", skills:["React","Node.js"], experience:1, city:"Bangalore", applied_on:new Date("2025-07-18") },
{ applicant_id:105, name:"Sereesha", skills:["AWS","Docker"], experience:5, city:"Kolkata", applied_on:new Date("2025-07-19") }
])

 // 3. applications – applicant_id, job_id, application_status, interview_scheduled, feedback

db.applications.insertMany([
{ application_id:1, applicant_id:101, job_id:1, application_status:"Pending", interview_scheduled:false, feedback:null },
{ application_id:2, applicant_id:102, job_id:2, application_status:"Shortlisted", interview_scheduled:true, feedback:"Good SQL skills" },
{ application_id:3, applicant_id:103, job_id:5, application_status:"Rejected", interview_scheduled:false, feedback:"Lacks DevOps experience" },
{ application_id:4, applicant_id:104, job_id:4, application_status:"Pending", interview_scheduled:false, feedback:null },
{ application_id:5, applicant_id:105, job_id:5, application_status:"Shortlisted", interview_scheduled:true, feedback:"Strong AWS background" },{ application_id:6, applicant_id:101, job_id:6, application_status:"Pending", interview_scheduled:false, feedback:null },
  { application_id:7, applicant_id:102, job_id:7, application_status:"Pending", interview_scheduled:false, feedback:null },
  { application_id:8, applicant_id:101, job_id:8, application_status:"Shortlisted", interview_scheduled:true, feedback:"Excellent fit" }
])

// Part 2: Write the Following Queries
 // 1. Find all remote jobs with a salary greater than 10,00,000.
db.jobs.find({ job_type:"remote", salary:{ $gt:1000000 } })

 // 2. Get all applicants who know MongoDB.
db.applicants.find({ skills:"MongoDB" })

 // 3. Show the number of jobs posted in the last 30 days.
db.jobs.countDocuments({ posted_on: { $gte: new Date(Date.now() - 30*24*60*60*1000) } })

 // 4. List all job applications that are in ‘interview scheduled’ status.
db.applications.find({ interview_scheduled:true })

 // 5. Find companies that have posted more than 2 jobs.
db.jobs.aggregate([
  { $group:{ _id:"$company", job_count:{ $sum:1 } } },
  { $match:{ job_count:{ $gt:2 } } }
])

// Part 3: Use $lookup and Aggregation
 // 6. Join applications with jobs to show job title along with the applicant’s name.
db.applications.aggregate([
  { $lookup:{ from:"jobs", localField:"job_id", foreignField:"job_id", as:"job" } },
  { $lookup:{ from:"applicants", localField:"applicant_id", foreignField:"applicant_id", as:"applicant" } },
  { $unwind:"$job" },
  { $unwind:"$applicant" },
  { $project:{ job_title:"$job.title", applicant_name:"$applicant.name", _id:0 } }
])

 // 7. Find how many applications each job has received.
db.applications.aggregate([
  { $group:{ _id:"$job_id", application_count:{ $sum:1 } } }
])

 // 8. List applicants who have applied for more than one job.
db.applications.aggregate([
  { $group:{ _id:"$applicant_id", count:{ $sum:1 } } },
  { $match:{ count:{ $gt:1 } } },
  { $lookup:{ from:"applicants", localField:"_id", foreignField:"applicant_id", as:"applicant" } },
  { $unwind:"$applicant" },
  { $project:{ name:"$applicant.name", count:1, _id:0 } }
])

 // 9. Show the top 3 cities with the most applicants.
db.applicants.aggregate([
  { $group:{ _id:"$city", applicant_count:{ $sum:1 } } },
  { $sort:{ applicant_count:-1 } },
  { $limit:3 }
])

 // 10. Get the average salary for each job type (remote, hybrid, on-site).
db.jobs.aggregate([
  { $group:{ _id:"$job_type", avg_salary:{ $avg:"$salary" } } }
])

 // Part 4: Data Updates
 // 11. Update the status of one application to "offer made".
db.applications.updateOne({}, { $set:{ application_status:"offer made" } })

 // 12. Delete a job that has not received any applications.
db.jobs.deleteMany({ _id: { $nin: db.applications.distinct("job_id") } })

 // 13. Add a new field  shortlisted to all applications and set it to false.
db.applications.updateMany({}, { $set:{ shortlisted:false } })

 // 14. Increment experience of all applicants from "Hyderabad" by 1 year.
db.applicants.updateMany({ city:"Hyderabad" }, { $inc:{ experience:1 } })

 // 15. Remove all applicants who haven’t applied to any job
db.applicants.deleteMany({ _id: { $nin: db.applications.distinct("applicant_id") } })
