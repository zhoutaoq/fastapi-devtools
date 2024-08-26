from enum import IntEnum


class UserStatus(IntEnum):
    ACTIVE = 1  # 活跃
    INACTIVE = 2  # 非活跃
    SUSPENDED = 3  # 暂停
    PENDING = 4  # 待处理
    BANNED = 5  # 封禁
    DELETED = 6  # 删除

    @classmethod
    def get_active_statuses(cls):
        return [cls.ACTIVE, cls.PENDING]

    @classmethod
    def get_inactive_statuses(cls):
        return [cls.INACTIVE, cls.SUSPENDED, cls.BANNED]

    @property
    def is_active(self):
        return self in self.get_active_statuses()

    @property
    def can_login(self):
        return self in [self.ACTIVE, self.PENDING]


# # 使用示例
# user_status = UserStatus.ACTIVE
# print(user_status.is_active)  # True
# print(user_status.can_login)  # True
#
# # 在查询中使用
# active_users = session.query(UserModel).filter(UserModel.status.in_(UserStatus.get_active_statuses())).all()


class MembershipType(IntEnum):
    FREE = 0  # 免费会员，基础功能访问
    BASIC = 1  # 基础会员，略微提升的功能和权限
    PREMIUM = 2  # 高级会员，大部分高级功能和优先支持


class SocialPlatform(IntEnum):
    WECHAT = 1  # 微信
    QQ = 2  # QQ
    WEIBO = 3  # 微博
    ALIPAY = 4  # 支付宝
    GITHUB = 5  # GitHub
    GOOGLE = 6  # 谷歌
    FACEBOOK = 7  # 脸书
    TWITTER = 8  # 推特
    LINKEDIN = 9  # 领英
    APPLE = 10  # 苹果
