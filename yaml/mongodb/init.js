// connect to admin database to create users
db = new Mongo().getDB("admin");
// create admin user
db.createUser({
  user: "adminCluster",
  pwd: "secret-pass",
  roles: [{
    role: "clusterAdmin",
    db: "admin"
  }]
});
// authenticate with admin user
db.auth("adminCluster", "secret-pass");
// switch to pois database
db = db.getSiblingDB("pois");
// create non admin user in pois database (used in app)
db.createUser({
  user: "user1",
  pwd: "pass1",
  roles: [{
    role: "dbOwner",
    db: "pois"
  }]
});