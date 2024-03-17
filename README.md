Nonogram Solver
===============

## 어떻게 입력을 받지?
```cmd
가로 방향 숫자를 한 줄에 한 열씩 입력하고 엔터를 치세요. 세로 방향을 입력하려면 / 를 입력하세요.
3
4
5
4
6
3 2 1
2 2 5
4 2 6
8 2 3
2 6 2 1
4 6
2 4
1 
/
세로방향 숫자를 한 줄에 한 행씩 입력하고 엔터를 치세요. 끝나면 . 을 입력하세요.
3
5
4 3
7
5
3
5
1 8
3 3 3 
7 3 2
5 4 2
8 2
10
2 3
6
```

## 내부 데이터는 어떻게 구성?
모델은 아래와 같이 2차원 리스트로 구성하고, 모든 칸을 0으로 채워뒀다가 색칠을 하면 1로 바꾸는 방식으로 구성 
```python
'-' = 미정, 칠해지지 않음
'O' = 확정, 칠해짐
'X' = 확정, 칠해지면 안됨
[
    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0]
    ...
]
```

## 해결 순서는 어떻게?
1. 가로 방향으로 가면서 채울 수 있는 칸은 모두 O로 채운다. 채워지지 않아야 할 칸은 2. 모두 X 로 채운다. 그 줄이 모두 채워졌으면 그 줄은 완료로 표시한다.
2. 가로를 모두 채우고 나면 세로 방향으로 채운다. 
3. 빈 칸이 아니라 이미 확정된 O 또는 X 가 있을 때는 이걸 기준으로 채울 수 있는 곳과 채우지 않아야 할 곳을 계산한다.
4. 1-3을 반복하면서 모든 가로줄/세로줄이 완료 표시 되었으면 해결 완료. 
5. 가로세로를 모두 돌았지만 1개도 새로 O 또는 X를 입력하지 못했으면 해결 불가로 판단하고 해결 실패로 결과 출력. 
