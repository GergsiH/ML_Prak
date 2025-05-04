haskell_code = '''
import Control.Arrow (Arrow (first))
import Data.Char (chr)

main :: IO ()
main =
  putStrLn answer
  where
    answer = zipWith foo bar numbers
    foo = curry $ chr . uncurry (-) . first ((`mod` 1021) . e)
    bar = c1 : c2 : zipWith f bar (tail bar)

f :: Eq a => [a] -> [a] -> [a]
f x y
  | d1 `c` a x y = sb x y
  | a x y `c` d2 = a x y
  | otherwise = f x $ m x y

z :: [a]
z = []

s :: [()] -> [()]
s x = () : x

a :: Eq a => [a] -> [a] -> [a]
a x y | x == z = y
a (x : xs) y = a xs (x : y)

sb :: Eq a => [b] -> [a] -> [b]
sb x y | y == z = x
sb (_ : xs) (_ : ys) = sb xs ys

m :: (Eq a, Eq b) => [b] -> [a] -> [b]
m x y | y == z = z
m x (y : ys) = a x $ m x ys

c :: (Eq a, Eq b) => [b] -> [a] -> Bool
c _ y | y == z = True
c x _ | x == z = False
c (_ : xs) (y : ys) = c xs ys

e :: (Eq a, Num p) => [a] -> p
e x | x == z = 0
e (_ : xs) = (1 +) $ e xs

numbers = [153, 586, 819, 461, 354, 843, 263, 215, 564, 884, 548, 511, 139, 814, -16, 853, -73, 886, 921, 870, 926, 886, 784, 763, 589, 364, 20, 502, 650, 237, -49, 288, 373, 774, 203, 73, 378, 549, 4, 657, 777, 592, 396, 89, 543, 696, 322, 144, 562, 761, 304, 144, 546, 736, 307, 32, 436, 572, -4, 618, 715, 462, 245, 762, -2, 856, 965, 833, 734]

c1 = s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s z

c2 = s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s z

d1 = s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s z

d2 = s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s $ s z

'''


def count_s(var_name):
    lines = haskell_code.splitlines()
    total = 0
    recording = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(f"{var_name} ="):
            recording = True
        if recording:
            total += line.count('s')
            # считаем, что определение заканчивается, когда строчка оканчивается на "z"
            if stripped.endswith("z"):
                break
    if not recording:
        raise ValueError(f"Не нашёл определение {var_name}")
    return total

c1_len = count_s('c1')
c2_len = count_s('c2')
d1_len = count_s('d1')
d2_len = count_s('d2')

print("c1_len =", c1_len)
print("c2_len =", c2_len)
print("d1_len =", d1_len)
print("d2_len =", d2_len)


def a_len(x, y):   return x + y
def sb_len(x, y):  return x - y
def m_len(x, y):   return x * y
def c_len(x, y):   return x >= y

def f_len(x, y):
    if c_len(d1_len, a_len(x, y)):
        return sb_len(x, y)
    elif c_len(a_len(x, y), d2_len):
        return a_len(x, y)
    else:
        return f_len(x, m_len(x, y))

numbers = [153, 586, 819, 461, 354, 843, 263, 215, 564, 884, 548, 511, 139, 814, -16, 853, -73, 886, 921, 870, 926, 886, 784, 763, 589, 364, 20, 502, 650, 237, -49, 288, 373, 774, 203, 73, 378, 549, 4, 657, 777, 592, 396, 89, 543, 696, 322, 144, 562, 761, 304, 144, 546, 736, 307, 32, 436, 572, -4, 618, 715, 462, 245, 762, -2, 856, 965, 833, 734]


bar = [c1_len, c2_len]
for i in range(2, len(numbers)):
    bar.append(f_len(bar[i-2], bar[i-1]))


message = ''.join(
    chr((bar[i] % 1021) - numbers[i])
    for i in range(len(numbers))
)

print("\nПолученный текст сообщения:\n")
print(message)