import json

employees = {}
zones = {}
file_name = "data.json"

#创建默认json文件
def create_json_file(file_name, data):
    try:
        with open(file_name, "w") as file:
            json.dump(data, file)
        print("JSON文件创建成功！")
    except Exception as e:
        print("创建JSON文件时出现错误：", str(e))

# 检测json是否存在
def check_file_exist(file_name):
    try:
        with open(file_name, "r") as file:
            # 文件成功打开，执行后续操作
            print(f"成功打开文件：{file_name}")
    except FileNotFoundError:
        # 文件不存在
        print(f"文件不存在：{file_name}")
        create_json_file(file_name, data)
    except Exception as e:
        # 其他错误
        print(f"打开文件时出现错误：{str(e)}")


#默认json
data = {
    "employees": {},
    "zones": {
        "01-综合区-外": {
            "初始数值": {
                "游览时长": 250,
                "科普价值": 190,
                "吸引人流": 240
            },
            "目标数值": {
                "游览时长": 375,
                "科普价值": 295,
                "吸引人流": 460
            }
        },
        "02-综合区-内": {
            "初始数值": {
                "游览时长": 270,
                "科普价值": 180,
                "吸引人流": 160
            },
            "目标数值": {
                "游览时长": 430,
                "科普价值": 356,
                "吸引人流": 275
            }
        },
        "03-工业区": {
            "初始数值": {
                "游览时长": 140,
                "科普价值": 240,
                "吸引人流": 190
            },
            "目标数值": {
                "游览时长": 270,
                "科普价值": 370,
                "吸引人流": 355
            }
        },
        "04-历史区": {
            "初始数值": {
                "游览时长": 200,
                "科普价值": 220,
                "吸引人流": 190
            },
            "目标数值": {
                "游览时长": 305,
                "科普价值": 315,
                "吸引人流": 345
            }
        }
    }
}



# 模式1：存入每个工作人员信息
def store_employee_data(employees):
    while True:
        employee_id = input("请输入员工姓名（输入0结束）：")
        if employee_id == '0':
            break
        
        employee_info = {}
        employee_info['游览时长'] = int(input("请输入游览时长属性值："))
        employee_info['科普价值'] = int(input("请输入科普价值属性值："))
        employee_info['吸引人流'] = int(input("请输入吸引人流属性值："))
        # 添加其他员工信息字段及其输入逻辑
        
        # 将新员工数据存入员工字典
        employees[employee_id] = employee_info
    
    return employees


# 模式2：存入四个区域的初始数值和目标值
def store_zone_values(zones):
    areas = ["01-综合区-外", "02-综合区-内", "03-工业区", "04-历史区"]

    for idx, area in enumerate(areas, start=1):
        print(f"{idx}. {area}")

    while True:
        try:
            choice = int(input("请选择要修改的区域序号（输入0结束）："))
            if choice == 0:
                break

            if choice < 1 or choice > len(areas):
                raise ValueError()
            
            zone_name = areas[choice - 1]
            print(f"\n当前选择的区域：{zone_name}")
            print(f"当前{zone_name}区域的属性：")
            print(f"初始数值：{zones[zone_name]['初始数值']}")
            print(f"目标数值：{zones[zone_name]['目标数值']}")

            confirm = input("是否要修改该区域的属性？（Y/N）：")
            if confirm.upper() == "Y":
                initial_values = {
                    "游览时长": int(input("请输入初始游览时长属性值：")),
                    "科普价值": int(input("请输入初始科普价值属性值：")),
                    "吸引人流": int(input("请输入初始吸引人流属性值："))
                }
                target_values = {
                    "游览时长": int(input("请输入目标游览时长属性值：")),
                    "科普价值": int(input("请输入目标科普价值属性值：")),
                    "吸引人流": int(input("请输入目标吸引人流属性值："))
                }

                zone_data = {
                    "初始数值": initial_values,
                    "目标数值": target_values
                }
                zones[zone_name] = zone_data

        except ValueError:
            print("输入无效，请输入正确的区域序号。")

    return zones



#模式3：修改删除数据
#显示列表
def list_employees(employees):
    print("已存储的员工：")
    for i, employee in enumerate(employees, start=1):
        print(f"{i}. {employee}")
    
    return employees

#修改或删除
def modify_or_delete_employee_data(employees, employee_number):
    employee_index = employee_number - 1

    if employee_index < 0 or employee_index >= len(employees):
        print("无效的员工序号")
        return employees

    employee_id = list(employees.keys())[employee_index]
    employee_info = employees[employee_id]

    # 显示当前员工信息
    print("当前员工信息：")
    print(f"员工姓名: {employee_id}")
    print(f"游览时长属性值: {employee_info['游览时长']}")
    print(f"科普价值属性值: {employee_info['科普价值']}")
    print(f"吸引人流属性值: {employee_info['吸引人流']}")

    choice = input("请选择要进行的操作（1、修改；2、删除；0、什么都不做）：")

    if choice == '1':
        # 修改员工信息
        employee_info['游览时长'] = int(input("请输入新的游览时长属性值："))
        employee_info['科普价值'] = int(input("请输入新的科普价值属性值："))
        employee_info['吸引人流'] = int(input("请输入新的吸引人流属性值："))
        print("已成功修改员工信息。")
    elif choice == '2':
        # 删除员工
        del employees[employee_id]
        print("已成功删除该员工。")

    return employees


def main():
    employees = None
    zones = None
    check_file_exist(file_name)
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 获取员工数据和区域数值
    employees = data['employees']
    zones = data['zones']
    
    while True:
        mode = int(input("请选择模式（1、存入工作人员信息；2、存入区域数值；3、列出已存储的员工名和序号；0、跳过存入）："))
        
        if mode == 1:
            employees = store_employee_data(employees)  # 将旧的员工数据传递给函数
            print("已成功存储工作人员信息。")
        elif mode == 2:
            zones = store_zone_values(zones)
            print("已成功存储区域数值。")
        elif mode == 3:
            list_employees(employees)
            employee_number = int(input("请输入员工序号："))
            if employee_number < 1 or employee_number > len(employees):
                print("无效的员工序号！")
            else:
                modify_or_delete_employee_data(employees, employee_number)
        elif mode == 0:
            break

    # 将更新后的员工数据和区域数值保存回文件
    data['employees'] = employees
    data['zones'] = zones
    
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


    # 从JSON文件中读取数据
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 获取员工数据和区域数值
    employees = data['employees']
    zones = data['zones']

    # 打印数据，这里只是做个快速的预览，存错了可以用读取.py列出来核对
    print(employees)
    print(zones)

main()

