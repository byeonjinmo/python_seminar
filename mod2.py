import mod1		# 같은 경로 py 모듈인 mod1.py의 함수인 mod1을 불러오는 import
result = mod1.add(3, 4)  # 7

 
from mod1 import add	# 특정 함수만 불러오기
result = add(3, 4)  # 모듈명 없이 직접 사용
print(result)
 
from mod1 import add, sub	# 여러 함수 불러오는 방법

from mod1 import *  # 모든 함수/변수를 가져옴