# Pf/main.py
import module.mymodule

# 객체 생성
calc = module.mymodule.FourCal()
calc.setdata(5, 3)
print("덧셈 결과:", calc.add())   # ✅ 인자 없이 호출
print("덧셈 결과:", calc.mul())
