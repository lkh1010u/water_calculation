water_feature = ['산성', '중성', '염기성']
print('용액의 성질 계산기')
while True:
  base = float(input('(1) 염기성 용액 양(ml): '))
  acid = float(input('(2) 산성 용액 양(ml): '))
  if base <= 0 or acid <= 0:
    print('⚠️ 두 용액의 양 모두 양수로 다시 입력해 주세요.\n')
  else:
    break
def water_calculation():
  volume = acid - base
  if volume > 0:
    result = water_feature[0]
  elif volume == 0:
    result = water_feature[1]
  else:
    result = water_feature[2]
  total_volume = base + acid
  print('_______________')
  print(f'용액의 성질: {result}')
  print(f'총 부피: {total_volume}ml')
water_calculation()
