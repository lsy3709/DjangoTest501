from django.db import models

# Create your models here.

# 앱만들기 명령어
# python manage.py startapp burgers

#실제로 데이터베이스 반영이되는 클래스,
# 스프링, 엔티티 클래스와 동일함.
# 클래스를 정의를 하면, 자동으로 테이블을 생성해줌. ORM
# 변경된 테이블 시스템에 적용하기.
# python manage.py migrate
# python manage.py makemigrations burgers
# python manage.py migrate burgers
class Burger(models.Model):
    # name , 필드, 데이터 타입으로 문자열 , 길이 100자
    name = models.CharField(max_length=100)
    # price , 가격 , 데이터 타입 정수로 , 기본값 0
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    # 해당 인스턴스를 출력시 나타나는 이름.
    def __str__(self):
        return self.name