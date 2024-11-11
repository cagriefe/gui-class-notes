# Setup the database
import dblib
# Create an instance of the GradeBookDatabase class
gradebook_db = dblib.GradeBookDatabase()
# Create the GradeBook table
gradebook_db.create_table()
# Fill the GradeBook table with initial data
gradebook_db.fill_data()

