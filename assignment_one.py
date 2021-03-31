#Get input from user

def average_function():
    user_entries = input('Please enter the numbers, separated with space, to get average: ')
    if user_entries:
        user_collection = user_entries.split(' ')
        
        total = 0
        for item in user_collection:
            total += float(item)
        avg = total/len(user_collection)
        print('The average of '+ user_entries + ' is ' + str(avg))
            
    else:
        print('You did not type anything')

    print("\n")

    from pythonfile3 import menu
    menu()


#     C:\Users\USER\Documents\UNIVELCITY\Programs\my_project>git status
# On branch main
# Your branch is up to date with 'origin/main'.

# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         modified:   README.md


# C:\Users\USER\Documents\UNIVELCITY\Programs\my_project>git commit -m "for all"
# [main feb3a03] for all
#  1 file changed, 2 insertions(+)

# C:\Users\USER\Documents\UNIVELCITY\Programs\my_project>git push origin main
# Enumerating objects: 5, done.
# Counting objects: 100% (5/5), done.
# Delta compression using up to 4 threads
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
# Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
# remote: Resolving deltas: 100% (1/1), completed with 1 local object.
# To https://github.com/mercyonanike1/my_project.git
#    fe874e3..feb3a03  main -> main

# C:\Users\USER\Documents\UNIVELCITY\Programs\my_project>git status
# On branch main
# Your branch is up to date with 'origin/main'.

# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   README.md

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         Git_hub_python.py

# no changes added to commit (use "git add" and/or "git commit -a")

# C:\Users\USER\Documents\UNIVELCITY\Programs\my_project>git status
# On branch main
# Your branch is up to date with 'origin/main'.

# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   README.md

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         Git_hub_python.py

# no changes added to commit (use "git add" and/or "git commit -a")

# C:\Users\USER\Documents\UNIVELCITY\Programs\my_project>git add "Git_hub_python.py"

# C:\Users\USER\Documents\UNIVELCITY\Programs\my_project>git commit -m "added a python file"
# [main 023966d] added a python file
#  1 file changed, 1 insertion(+)
#  create mode 100644 Git_hub_python.py

# C:\Users\USER\Documents\UNIVELCITY\Programs\my_project>git push origin main
# Enumerating objects: 4, done.
# Counting objects: 100% (4/4), done.
# Delta compression using up to 4 threads
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (3/3), 326 bytes | 326.00 KiB/s, done.
# Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
# To https://github.com/mercyonanike1/my_project.git
#    feb3a03..023966d  main -> main

# C:\Users\USER\Documents\UNIVELCITY\Programs\my_project>
















































