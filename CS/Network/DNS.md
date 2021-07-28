# DNS(Domain Name System)

## Internet에서의 ID(기계)

### IP

- IPv4: 32bit(8bit *4 ) (xxx.xxx.xxx.xxx)
- IPv6: 128bit(16bit * 8) (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx)

### Domain Name

- 순수하게 인간을 위한 시스템
- 응용계층(인터넷 5계층)에서만 관여

## Domain Name System

- 서비스
  - Domain Name -> IP 주소
  - Aliasing 관리
  - 전우주적으로 중앙 관리
  - 분산 관리(계층적 분산 관리)
- Domain Name server의 계층
  - 최상위: Root Name Server
    - Top-level Domain Name Server 관리
      - Top-level Domain = [.kr, .com, .edu, .org, .net]
    - Top-level Domain Server의 IP를 반환(유효기간과 함께)
    - 유효기간 동안은 동일한 Top-level Domain Server IP 요청을 하지 않는다.
    - 컴퓨터 -> Local DNS -> Authorized DNS -> Top-level DNS -> Root DNS



# P2P(Peer-to-Peer)

- 서버없이 단말(Peer)들끼리 직접상호간 서비스를 제공하는 시스템
- 서비스가 보장되지 않는다.
- Peer들은 ID를 바꾸며 옮겨 다닐 수 있다.

## Hybrid System

- 서비스 메타 정보를 서버가 관리
- 실제적 서비스는 Peer 끼리
- Skype, 스타크래프트 (서버가 연결만 해주고 연결된 뒤에는 Peer끼리)

## Pure P2P

- Torrent
- 문제
  - Peer가 없다.
  - 신뢰가 어렵다 - 해쉬 코드를 이용하여 해결
  - 이기적
  - 조각들의 쏠림 현상



# 번외

## 인터넷 5계층 관점에서 응용 계층에서만 도메인을 사용하고 그 밑으로는 IP 주소를 사용한다.