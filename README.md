I used Antigravity AI to generate Django code components.

 Create Student Model
Create a Django model named Student with fields:
name (CharField), email (EmailField with unique=True),
course_interest (CharField),
status (CharField with choices: Applied, Interviewing, Accepted, Rejected).
Add __str__ method to return student name


 Create Views
Generate Django class-based views

 StudentListView using ListView
Show all students
 Add search functionality using GET parameter 
 Filter students by course_interest using icontains

 StudentCreateView using CreateView
 Use ModelForm
Redirect to student list after successful submission

 Create ModelForm
Create a Django ModelForm named StudentForm
for the Student model including all fields

Create URLs
Create URL patterns for
 Home page → student list
/add/ → student creation form

Create Templates
 base.html layout
student_list.html
 Show students in table
Add search input field
student_form.html
   Display student form
   Add submit button
