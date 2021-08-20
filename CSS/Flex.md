# Flex

- Flex를 사용하기 위해서는 태그가 두 단계가 필요하다

  ```html
  <container>
  	<item></item>
    <item></item>
  </container>
  ```

  

| container       | item        |
| --------------- | ----------- |
| display         | order       |
| flex-direction  | flex-grow   |
| flex-wrap       | flex-shrink |
| flex-flow       | flex-basis  |
| justify-content | flex        |
| align-items     | align-self  |
| align-content   |             |

## flex-wrap

1. nowrap
2. wrap = container의 크기보다 item의 크기가 크면 줄바꿈 된다.
3. wrap-reverse = wrap 반대로



## align-items (위 아래 위치 조정)

1. flex-start = 각각의 아이템들이 자신의 컨텐트 크기에 맞는 크기를 갖고 처음부분에 정렬
2. flex-end = 각각의 아이템들이 자신의 컨텐트 크기에 맞는 크기를 갖고 끝부분에 정렬
3. center = 각각의 아이템들이 자신의 컨텐트 크기에 맞는 크기를 갖고 가운데 부분에 정렬
4. baseline = 아이템들의 컨텐트의 밑줄을 한 줄에 맞춰서 정렬
5. stretch =



## justify-content (오른쪽 왼쪽 위치 조정)

1. flex-start = 아이템들을 왼쪽으로 배치
2. flex-end = 아이템들을 오른쪽으로 배치
3. space-between = 
4. center = 아이템들을 가운데 배치
5. space-around



## align-content

#### 같은 행에 있는 아이템들을 하나의 그룹으로 인식하고 그룹과 그룹 사이의 정렬을 결정한다.

1. flex-start
2. flex-end
3. center
4. space-between
5. space-around
6. stretch

# Properties for the flex items

## align-self

### 특정한 아이템만 예외적으로 다르게 값을 주고 싶을 때 사용

1. auto
2. flex-start
3. flex-end
4. center
5. baseline
6. stretch



## flex

```css
.item { flex: flex-grow [flex-shrink] [flex-basis]; }
```



## order

#### flex 내의 아이템 순서 배치를 바꿀 수 있다.