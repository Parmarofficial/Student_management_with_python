from databases import get_connection

# Add course
def add_courses(name):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO courses (name) VALUES (%s)"
    cursor.execute(query, (name,))
    conn.commit()
    conn.close()
    print("Course added successfully!")

# View all courses
def view_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Courses ---")
    for row in rows:
        print(row)
