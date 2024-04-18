def read_single_digit(digit):
  korean_digits = {
    '0': '영',
    '1': '일',
    '2': '이',
    '3': '삼',
    '4': '사',
    '5': '오',
    '6': '육',
    '7': '칠',
    '8': '팔',
    '9': '구'
  }
  return korean_digits[digit]

def read_number(number):
  korean_units = {
    '0': '',
    '1': '십',
    '2': '백',
    '3': '천'
  }

def main():
  number = int(input("세 자리수 이하의 10진 정수를 입력하세요: "))
  print(read_number(number))
