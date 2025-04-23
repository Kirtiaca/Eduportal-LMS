from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Assignment, Submission
from .forms import AssignmentForm, SubmissionForm

# Teacher: Create Assignment
@login_required
def create_assignment(request):
    if request.user.profile.role == "teacher":
        if request.method == "POST":
            form = AssignmentForm(request.POST)
            if form.is_valid():
                assignment = form.save(commit=False)
                assignment.teacher = request.user  # Assign teacher
                assignment.save()
                print("✅ Assignment Created:", assignment)  # Debugging
                return redirect('assignment_list')
            else:
                print("❌ Form Errors:", form.errors)  # Debugging
        else:
            form = AssignmentForm()
        return render(request, 'assignments/assignments.html', {'form': form, 'assignments': Assignment.objects.all()})  
    return redirect('assignment_list')

# Student & Teacher: View Assignments
@login_required
def assignment_list(request):
    if request.user.profile.role == "teacher":
        assignments = Assignment.objects.filter(teacher=request.user)
    else:
        assignments = Assignment.objects.all()
    
    print("📢 Assignments Fetched:", assignments)  # Debugging
    return render(request, 'assignments/assignments.html', {'assignments': assignments})

# Student: Submit Assignment
@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.student = request.user
            submission.assignment = assignment
            submission.save()
            return redirect('assignment_list')
    return redirect('assignment_list')

# Teacher: View Submissions
@login_required
def view_submissions(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    submissions = Submission.objects.filter(assignment=assignment)  # Fetch related submissions
    return render(request, "assignments/assignments.html", {"assignment": assignment, "submissions": submissions})

# Teacher: Delete Assignment
@login_required
def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id, teacher=request.user)
    if request.method == "POST":
        assignment.delete()
        return redirect('assignment_list')
    return redirect('assignment_list')