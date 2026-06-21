class Course:
    def __init__(self, title, description, instructor, duration, topics=None):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration
        self.topics = topics or []

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"

courses = [
    Course("Python Mastery: From Zero to Developer", "Learn the basics of Python programming.", "John Doe", "4 weeks"),
    Course("Full-Stack Python: Real-World Web Apps with Flask", "Build web applications using Flask.", "Jane Smith", "6 weeks"),
    Course("Data Science in Practice: From Data to Insights", "An introduction to data science concepts and tools.", "Alice Johnson", "8 weeks"),
    Course("Go in Action: Concurrency & Performance for Modern Developers", "Master Go's powerful concurrency model, type system, and performance-focused toolchain to build reliable backend services.", "Bob Chen", "6 weeks"),
]