#utilize bash to add, commit and push to branch/repo
git add .
#input comment before pushing
echo 'input comment:'
read comment
#Commit with comment
git commit -m "$comment"
#specify which branch to push to
echo 'Enter the name of the branch:'
read branch

git push origin $branch

read