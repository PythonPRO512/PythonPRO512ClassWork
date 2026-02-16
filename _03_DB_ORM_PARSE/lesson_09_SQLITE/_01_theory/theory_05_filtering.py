import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\students.db')
    cursor = conn.cursor()

    # fetchall() — получает все строки из результата запроса.
    subjects = ['Математика', 'Химия']
    courses_students = []
    for subj in subjects:
        cursor.execute('SELECT * FROM students WHERE course = ?', (subj,))
        course_students = cursor.fetchall()
        courses_students.append(course_students)

    print(courses_students)
    conn.close()
