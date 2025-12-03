from databases import get_connection

#to add student 
def add_student(name, email, phone, age):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO students (name, email, phone, age) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, email, phone, age))

    conn.commit()
    conn.close()
    print("Student added successfully!")


#to view student record
def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


#to update the student record
def update_student(id, name, email, phone, age):
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE students SET name=%s, email=%s, phone=%s, age=%s WHERE id=%s"
    cursor.execute(query, (name, email, phone, age, id))

    conn.commit()
    conn.close()


#to delete the student record
def delete_student(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()

    conn.close()
