#-*- coding:utf-8 -*- 
 
######学生基本信息 
#姓名：郭金 
#学号：1403050208 
#班级：通风14-2班 
 
###########题目############### 
import math 

 a = float(raw_input('Input a: ')) 
 b = float(raw_input('Input a: ')) 
 c = float(raw_input('Input a: ')) 
  
 root = math.sqrt(b ** 2 - 4 * a * c) 
 s1 = (-b + root) / (2 * a) 
 s2 = (-b + root) / (2 * a) 
 
 print 'The solutions are:', s1, s2 
