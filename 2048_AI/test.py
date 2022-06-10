students = []  # 用于存储所有学生的列表（实际项目中，数据是存储在数据库中的）


# 根据学号检查学生是否存在
def is_exists(sid):
    for student_dict in students:
        student_id = student_dict.get("stu_id")  # 获取当前正在遍历的学生的ID
        if sid == student_id:
            return True  # 查到了，说明系统存在该生，返回True
    return False  # 没查到


# 添加新生的函数
def add_student(sid, name, score):
    # 添加学生之前应该先检查该生是否已经存在于系统中（根据学号判断是否存在）
    is_have = is_exists(sid)
    if is_have:
        return False
    # 创建新生字典
    new_student = {
        "stu_id": sid,
        "stu_name": name,
        "stu_score": score
    }
    students.append(new_student)  # 将新生添加到学生列表中
    return True


# 删除新生函数
def delete_student(sid):
    # 删除学生之前应该先检查该生是否已经存在于系统中（根据学号判断是否存在）
    is_have = is_exists(sid)
    if is_have:
        deleted_student = {
            "stu_id": sid,
            "stu_name": name,
            "stu_score": score
        }
    students.remove(deleted_student)
    return True


# 查询单个学生信息
def showONE(sid):
    is_have = is_exists(sid)
    if is_have:
        # student_sid = input("需查询学生学号：")
        print(student_dict.get("stu_name"), student_dict.get("stu_score"))
    return True


# 查询所有学生的信息
def showAll():
    for student_dict in students:
        print(student_dict.get("stu_id"), student_dict.get("stu_name"), student_dict.get("stu_score"))


if __name__ == '__main__':  # __name__代表调用该文件的名称，保护作用
    while True:
        choice = input("请选择：1 添加新生 2 删除新生 3 查看某个学生 4 显示所有学生 5 退出系统")
        if choice == "1":
            new_sid = input("新生学号：")
            new_name = input("新生姓名：")
            new_score = float(input("新生成绩："))  # 如果输入非数字，此处会报错，可以加入异常机制处理
            is_successful = add_student(new_sid, new_name, new_score)
            if is_successful:
                print("新生添加成功~~~~")
            else:
                print("该生已经存在于系统，添加失败！")
        elif choice == "2":
            deleted_sid = input("删除学生学号：")
            deleted_name = ()
            deleted_score = ()
            is_successful = delete_student(deleted_sid, deleted_name, deleted_score)
            if is_successful:
                print("新生删除成功~")

            else:
                print("该生不存在于系统，删除失败！")

            elif choice == "3":
            student_sid = input("需查询学生学号：")

        elif choice == "4":
            print("学号\t姓名\t成绩\t")
            showAll()
        elif choice == "5":
            break
        else:
            print("无此选项，请重新选择！")
        else:
        print("该生不存在于系统，删除失败！")

    elif choice == "3":
    student_sid = input("需查询学生学号：")

elif choice == "4":
    print("学号\t姓名\t成绩\t")
    showAll()
elif choice == "5":
    break
else:
    print("无此选项，请重新选择！")
