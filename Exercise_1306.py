
# coding: utf-8

# In[1]:


'''
Cach 1: Su dung ham rfind('ki_tu_can_tim_trong_string'): tra ve phan tu can tim o vi tri cuoi cung trong chuoi, neu khong tim 
thay se tra ve -1
'''
import time
start = time.clock()
s = 'a.b.c.mp3'
a = s.rfind('.')
print(s[a+1:])
end = time.clock()
print('Time run : %s' %(end-start))


# In[2]:


'''
Cách 2: 
- Ép kiểu từ string sang list, đồng thời sử dụng hàm split để phân chia thành các phần tử được ngăn cách nhau bởi dấu phẩy.
- Sau đó đơn giản ta chỉ cần in phần tử nằm cuối cùng ở trong list đó. 
'''
import time 
start = time.clock()
s = 'a.b.c.mp3'
a = s.split('.')
print(a[-1])
end = time.clock()
print('Time run: %s' %(end-start))

