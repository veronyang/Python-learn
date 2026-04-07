cd /python_basic_learn/python-basic-Homework

# 预览将要重命名的文件
for f in day*_homework_1.*.py; do echo "$f -> $(echo $f | sed 's/1\./1_/')"; done

# 正式执行重命名
for f in day*_homework_1.*.py; do mv "$f" "$(echo $f | sed 's/1\./1_/')"; done
