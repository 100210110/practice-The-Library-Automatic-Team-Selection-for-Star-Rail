import json

# 从JSON文件中读取数据
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 获取employees，zones字典
employees_dict = data['employees']
zones_dict = data['zones']
i = 0

# 打印数据
print(employees_dict)
print(zones_dict)
print()
print()

# 显示区域属性
for zone_id, zone_data in zones.items():
    print("区域名称:", zone_id)

    for subkey, subvalue in zone_data.items():
        print(subkey + ':')
        for key, value in subvalue.items():
            print(f"\t{key}: {value}")

    print("-" * 20)  # 在每个区域之间添加分界线

print()  # 看起来还……勉强易于分辨的分割线
print("-" * 30)
print()
print("-" * 20)

# 显示员工属性
for employee_id, values in employees_dict.items():
    i += 1
    print(f"第 {i} 名")
    print("员工姓名:", employee_id)
    for key, value in values.items():
        print(key, ":", value)
    print("-" * 20)  # 在员工之间添加分界线
input()
