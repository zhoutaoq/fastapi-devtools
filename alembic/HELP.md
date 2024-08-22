Alembic 是一个数据库迁移工具，主要用于 SQLAlchemy。它允许你管理和应用数据库模式的变更（迁移），使得数据库结构和应用程序代码保持同步。以下是如何使用 Alembic 操作数据库的步骤，包括安装、配置和执行迁移。
1. 安装 Alembic

首先，你需要安装 Alembic。如果你还没有安装，可以通过 pip 安装：
bash
pip install alembic

2. 初始化 Alembic

在你的项目根目录中，初始化 Alembic 以创建所需的配置文件和目录结构：
bash
alembic init alembic

这会创建一个 alembic 目录，其中包含一个 env.py 文件和 versions 目录，以及一个 alembic.ini 配置文件。
3. 配置 Alembic

在 alembic.ini 文件中，设置数据库连接字符串：
ini
[alembic]
script_location = alembic
sqlalchemy.url = sqlite:///./mydatabase.db

将 sqlalchemy.url 替换为你的数据库连接字符串。例如，对于 PostgreSQL，你的连接字符串可能如下所示：
ini
sqlalchemy.url = postgresql://user:password@localhost/mydatabase

4. 配置 env.py

在 alembic/env.py 中，配置你的 SQLAlchemy Base 类，以便 Alembic 能够识别模型并生成迁移脚本。确保你的模型类和 Base 在这个文件中可用：
python
from myapp.models import Base  # 导入你的模型Base类

target_metadata = Base.metadata

将 myapp.models 替换为包含你模型的模块。
5. 创建迁移脚本

使用 Alembic 生成新的迁移脚本。这个命令会比较当前的数据库模式与模型定义，生成一个新的迁移脚本：
bash
alembic revision --autogenerate -m "initial migration"

-m "initial migration" 是你对迁移脚本的描述，能够帮助你记住这次迁移的目的。
6. 编辑迁移脚本（如果需要）

迁移脚本会被生成在 alembic/versions 目录下。你可以手动编辑这些脚本以添加特定的数据库变更逻辑。例如，添加数据迁移或复杂的数据库操作。
7. 应用迁移

运行迁移脚本以将更改应用到数据库：
bash
alembic upgrade head

这会将数据库迁移到最新版本。如果你只想应用到特定版本，可以使用该版本的修订号：
bash
alembic upgrade <revision>

8. 回滚迁移

如果需要回滚最近的迁移，可以使用：
bash
alembic downgrade -1

这将回滚最近的一次迁移。如果你需要回滚到特定版本，可以使用该版本的修订号：
bash
alembic downgrade <revision>

9. 查看当前迁移状态

你可以检查数据库当前的迁移状态，了解已经应用了哪些迁移：
bash
alembic current

总结

安装 Alembic：pip install alembic
初始化 Alembic：alembic init alembic
配置 Alembic：编辑 alembic.ini 和 alembic/env.py
创建迁移脚本：alembic revision --autogenerate -m "description"
编辑迁移脚本（如需）
应用迁移：alembic upgrade head
回滚迁移（如需）：alembic downgrade -1
查看当前迁移状态：alembic current
