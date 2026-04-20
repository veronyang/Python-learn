"""
SQLAlchemy ORM 练习：设备 Inventory 系统
使用 SQLAlchemy ORM 制作一个网络设备资产管理系统，将设备信息存入 SQLite 数据库，并实现交互式查询菜单。

数据库模型字段：

id：主键，自动递增
name：设备名称（如 R1、SW1），带索引
type：设备类型（如 router、switch、firewall）
version：系统版本（如 IOS XE 17.14）
location：机房位置（如 Beijing-IDC-A）
create_time：入库时间，自动填写当前时间
"""

import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# 创建数据库引擎
engine = create_engine('sqlite:///device_inventory.db?check_same_thread=False',
                       echo=False)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Device(Base):
    __tablename__ = 'devices'

    id          = Column(Integer, primary_key=True)
    name        = Column(String(64), nullable=False, index=True)
    type        = Column(String(64), nullable=False)
    version     = Column(String(64))
    location    = Column(String(128))
    create_time = Column(DateTime(timezone='Asia/Chongqing'), default=datetime.datetime.now)

    def __repr__(self):
        return (f"{self.__class__.__name__}(设备名称: {self.name} | 类型: {self.type} | "
                f"版本: {self.version} | 位置: {self.location} | 入库时间: {self.create_time})")
    
def print_results(results):
    if results:
        for device in results:
            print(device)
    else:
        print("[-] 未找到匹配的设备")


if __name__ == '__main__':
    # 创建数据库表
    Base.metadata.create_all(engine, checkfirst=True)

    # 只有表为空时才插入初始数据
    if session.query(Device).count() == 0:
        device_list = [{'name': 'R1',  'type': 'router',   'version': 'IOS XE 17.14', 'location': 'Beijing-IDC-A'},
            {'name': 'R2',  'type': 'router',   'version': 'IOS XE 17.14', 'location': 'Shanghai-IDC-B'},
            {'name': 'SW1', 'type': 'switch',   'version': 'IOS 15.2',     'location': 'Beijing-IDC-A'},
            {'name': 'SW2', 'type': 'switch',   'version': 'IOS 15.2',     'location': 'Shanghai-IDC-B'},
            {'name': 'FW1', 'type': 'firewall', 'version': 'ASA 9.16',     'location': 'Beijing-IDC-A'},
            {'name': 'FW2', 'type': 'firewall', 'version': 'FTD 7.2',      'location': 'Shenzhen-IDC-C'}]

        for device in device_list:
            session.add(Device(**device))
        session.commit()

    while True:
        print("\n请输入查询选项:")
        print("输入 1：查询所有设备")
        print("输入 2：根据设备名称查询")
        print("输入 3：根据设备类型查询")
        print("输入 4：根据机房位置查询")
        print("输入 0：退出")

        while True:
            choice = input("\n请输入查询选项：").strip()
            if choice in ('0', '1', '2', '3', '4'):
                break
            print("无效的选项，请重新输入（0-4）")

        if choice == '1':
            results = session.query(Device).all()
            print_results(results)
            pass

        elif choice == '2':
            name = input("请输入设备名称：")
            results = session.query(Device).filter_by(name=name).all()
            print_results(results)
            pass

        elif choice == '3':
            device_type = input("请输入设备类型（router/switch/firewall）：")
            results = session.query(Device).filter_by(type=device_type).all()
            print_results(results)
            pass

        elif choice == '4':
            keyword = input("请输入机房位置关键词：")
            results = session.query(Device).filter(Device.location.contains(keyword)).all()
            print_results(results)
            pass

        elif choice == '0':
            break