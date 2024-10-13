Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: E:/Semester 3/Python practical/Extra/hello.world.py =========
> e:\semester 3\python practical\extra\hello.world.py(4)hello_world()
-> print("Hello World")
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) q
Traceback (most recent call last):
  File "E:/Semester 3/Python practical/Extra/hello.world.py", line 7, in <module>
    hello_world()
  File "E:/Semester 3/Python practical/Extra/hello.world.py", line 4, in hello_world
    print("Hello World")
  File "E:/Semester 3/Python practical/Extra/hello.world.py", line 4, in hello_world
    print("Hello World")
bdb.BdbQuit
>>> 
=== RESTART: E:/Semester 3/Python practical/Extra/Max3.py ===
> e:\semester 3\python practical\extra\max3.py(22)<module>()
-> maxVal = maximum(a, b, c)
(Pdb) p a
10
(Pdb) p maxVal
*** NameError: name 'maxVal' is not defined
(Pdb) n
> e:\semester 3\python practical\extra\max3.py(23)<module>()
-> print(maxVal)
(Pdb) p maxVal
14
(Pdb) n
14
--Return--
> e:\semester 3\python practical\extra\max3.py(23)<module>()->None
-> print(maxVal)
(Pdb) q
Traceback (most recent call last):
  File "E:/Semester 3/Python practical/Extra/Max3.py", line 23, in <module>
    print(maxVal)
bdb.BdbQuit
>>> 
=== RESTART: E:/Semester 3/Python practical/Extra/Max3.py ===
> e:\semester 3\python practical\extra\max3.py(22)<module>()
-> maxVal = maximum(a, b, c)
(Pdb) s
--Call--
> e:\semester 3\python practical\extra\max3.py(4)maximum()
-> def maximum(a, b, c):
(Pdb) s
> e:\semester 3\python practical\extra\max3.py(5)maximum()
-> if (a >= b) and (a >= c):
(Pdb) a
a = 10
b = 14
c = 12
(Pdb) n
> e:\semester 3\python practical\extra\max3.py(8)maximum()
-> elif (b >= a) and (b >= c):
(Pdb) n
> e:\semester 3\python practical\extra\max3.py(9)maximum()
-> largest = b
(Pdb) n
> e:\semester 3\python practical\extra\max3.py(13)maximum()
-> return largest
(Pdb) p largest
14
(Pdb) n
--Return--
> e:\semester 3\python practical\extra\max3.py(13)maximum()->14
-> return largest
(Pdb) n
> e:\semester 3\python practical\extra\max3.py(23)<module>()
-> print(maxVal)
(Pdb) q
Traceback (most recent call last):
  File "E:/Semester 3/Python practical/Extra/Max3.py", line 23, in <module>
    print(maxVal)
  File "E:/Semester 3/Python practical/Extra/Max3.py", line 23, in <module>
    print(maxVal)
bdb.BdbQuit
>>> 
=== RESTART: E:/Semester 3/Python practical/Extra/Max3.py ===
> e:\semester 3\python practical\extra\max3.py(22)<module>()
-> maxVal = maximum(a, b, c)
(Pdb) s
--Call--
> e:\semester 3\python practical\extra\max3.py(4)maximum()
-> def maximum(a, b, c):
(Pdb) s
> e:\semester 3\python practical\extra\max3.py(5)maximum()
-> if (a >= b) and (a >= c):
(Pdb) s
> e:\semester 3\python practical\extra\max3.py(8)maximum()
-> elif (b >= a) and (b >= c):
(Pdb) s
> e:\semester 3\python practical\extra\max3.py(9)maximum()
-> largest = b
(Pdb) s
> e:\semester 3\python practical\extra\max3.py(13)maximum()
-> return largest
(Pdb) s
--Return--
> e:\semester 3\python practical\extra\max3.py(13)maximum()->14
-> return largest
(Pdb) s
> e:\semester 3\python practical\extra\max3.py(23)<module>()
-> print(maxVal)
(Pdb) s
--Call--
> c:\python39\lib\idlelib\run.py(441)write()
-> def write(self, s):
(Pdb) s
> c:\python39\lib\idlelib\run.py(442)write()
-> if self.closed:
(Pdb) p
*** SyntaxError: unexpected EOF while parsing
(Pdb) q
Traceback (most recent call last):
  File "E:/Semester 3/Python practical/Extra/Max3.py", line 23, in <module>
    print(maxVal)
bdb.BdbQuit
>>> 
=== RESTART: E:/Semester 3/Python practical/Extra/Max3.py ===
> e:\semester 3\python practical\extra\max3.py(22)<module>()
-> maxVal = maximum(a, b, c)
(Pdb) n
> e:\semester 3\python practical\extra\max3.py(23)<module>()
-> print(maxVal)
(Pdb) n
14
--Return--
> e:\semester 3\python practical\extra\max3.py(23)<module>()->None
-> print(maxVal)
(Pdb) n
> c:\python39\lib\idlelib\run.py(561)runcode()
-> interruptable = False
(Pdb) q
Traceback (most recent call last):
** IDLE Internal Exception: 
  File "C:\Python39\lib\idlelib\run.py", line 561, in runcode
    interruptable = False
  File "C:\Python39\lib\idlelib\run.py", line 561, in runcode
    interruptable = False
  File "C:\Python39\lib\bdb.py", line 88, in trace_dispatch
    return self.dispatch_line(frame)
  File "C:\Python39\lib\bdb.py", line 113, in dispatch_line
    if self.quitting: raise BdbQuit
bdb.BdbQuit
>>> 
=== RESTART: E:/Semester 3/Python practical/Extra/Max3.py ===
> e:\semester 3\python practical\extra\max3.py(22)<module>()
-> maxVal = maximum(a, b, c)
(Pdb) s
--Call--
> e:\semester 3\python practical\extra\max3.py(4)maximum()
-> def maximum(a, b, c):
(Pdb) n
> e:\semester 3\python practical\extra\max3.py(5)maximum()
-> if (a >= b) and (a >= c):
(Pdb) a
a = 10
b = 14
c = 12
(Pdb) n
> e:\semester 3\python practical\extra\max3.py(8)maximum()
-> elif (b >= a) and (b >= c):
(Pdb) n
> e:\semester 3\python practical\extra\max3.py(9)maximum()
-> largest = b
(Pdb) n
> e:\semester 3\python practical\extra\max3.py(13)maximum()
-> return largest
(Pdb) p largest
14
(Pdb) n
--Return--
> e:\semester 3\python practical\extra\max3.py(13)maximum()->14
-> return largest
(Pdb) n
> e:\semester 3\python practical\extra\max3.py(23)<module>()
-> print(maxVal)
(Pdb) p maxVal
14
(Pdb) q
Traceback (most recent call last):
  File "E:/Semester 3/Python practical/Extra/Max3.py", line 23, in <module>
    print(maxVal)
  File "E:/Semester 3/Python practical/Extra/Max3.py", line 23, in <module>
    print(maxVal)
bdb.BdbQuit
>>> 
=== RESTART: E:/Semester 3/Python practical/Extra/Max3.py ===
> e:\semester 3\python practical\extra\max3.py(22)<module>()
-> maxVal = maximum(a, b, c)
(Pdb) l
 17  	a = 10
 18  	b = 14
 19  	c = 12
 20  	import pdb
 21  	pdb.set_trace()
 22  ->	maxVal = maximum(a, b, c)
 23  	print(maxVal)
[EOF]
(Pdb) ll
  1  	# Python program to find the largest
  2  	# number among the three numbers
  3  	
  4  	def maximum(a, b, c):
  5  		if (a >= b) and (a >= c):
  6  			largest = a
  7  	
  8  		elif (b >= a) and (b >= c):
  9  			largest = b
 10  		else:
 11  			largest = c
 12  	
 13  		return largest
 14  	
 15  	
 16  	# Driver code
 17  	a = 10
 18  	b = 14
 19  	c = 12
 20  	import pdb
 21  	pdb.set_trace()
 22  ->	maxVal = maximum(a, b, c)
 23  	print(maxVal)
(Pdb) b 14
*** Blank or comment
(Pdb) b 13
Breakpoint 1 at e:\semester 3\python practical\extra\max3.py:13
(Pdb) c
> e:\semester 3\python practical\extra\max3.py(13)maximum()
-> return largest
(Pdb) p largest
14
(Pdb) n
--Return--
> e:\semester 3\python practical\extra\max3.py(13)maximum()->14
-> return largest
(Pdb) 
=== RESTART: E:/Semester 3/Python practical/Extra/Max3.py ===
> e:\semester 3\python practical\extra\max3.py(22)<module>()
-> maxVal = maximum(a, b, c)
(Pdb) b14
*** NameError: name 'b14' is not defined
(Pdb) b13
*** NameError: name 'b13' is not defined
(Pdb) b 13
Breakpoint 1 at e:\semester 3\python practical\extra\max3.py:13
(Pdb) b 10
Breakpoint 2 at e:\semester 3\python practical\extra\max3.py:10
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:13
2   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:10
(Pdb) c
> e:\semester 3\python practical\extra\max3.py(13)maximum()
-> return largest
(Pdb) b 13
Breakpoint 3 at e:\semester 3\python practical\extra\max3.py:13
(Pdb) b 9
Breakpoint 4 at e:\semester 3\python practical\extra\max3.py:9
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:13
	breakpoint already hit 1 time
2   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:10
3   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:13
4   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:9
(Pdb) c
14
>>> c
12
>>> c
12
>>> b
14
>>> 
=== RESTART: E:/Semester 3/Python practical/Extra/Max3.py ===
> e:\semester 3\python practical\extra\max3.py(22)<module>()
-> maxVal = maximum(a, b, c)
(Pdb) b 13
Breakpoint 1 at e:\semester 3\python practical\extra\max3.py:13
(Pdb) b 9
Breakpoint 2 at e:\semester 3\python practical\extra\max3.py:9
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:13
2   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:9
(Pdb) disable 1
Disabled breakpoint 1 at e:\semester 3\python practical\extra\max3.py:13
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep no    at e:\semester 3\python practical\extra\max3.py:13
2   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:9
(Pdb) enable 1
Enabled breakpoint 1 at e:\semester 3\python practical\extra\max3.py:13
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:13
2   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:9
(Pdb) cl 9
*** Breakpoint number 9 out of range
(Pdb) cl2
*** NameError: name 'cl2' is not defined
(Pdb) cl 2
Deleted breakpoint 2 at e:\semester 3\python practical\extra\max3.py:9
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at e:\semester 3\python practical\extra\max3.py:13
(Pdb) q
Traceback (most recent call last):
  File "E:/Semester 3/Python practical/Extra/Max3.py", line 22, in <module>
    maxVal = maximum(a, b, c)
  File "E:/Semester 3/Python practical/Extra/Max3.py", line 22, in <module>
    maxVal = maximum(a, b, c)
bdb.BdbQuit
>>> q
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> 
==== RESTART: E:/Semester 3/Python practical/Extra/sum.py ===
> e:\semester 3\python practical\extra\sum.py(9)sum_of_list()
-> total_sum = 0
(Pdb) n
> e:\semester 3\python practical\extra\sum.py(10)sum_of_list()
-> for val in numbers:
(Pdb) n
> e:\semester 3\python practical\extra\sum.py(11)sum_of_list()
-> total_sum += val
(Pdb) n
> e:\semester 3\python practical\extra\sum.py(10)sum_of_list()
-> for val in numbers:
(Pdb) n
> e:\semester 3\python practical\extra\sum.py(11)sum_of_list()
-> total_sum += val
(Pdb) p total_sum
6
(Pdb) ll
  6  	def sum_of_list():
  7  	    import pdb
  8  	    pdb.set_trace()
  9  	    total_sum = 0
 10  	    for val in numbers:
 11  ->	        total_sum += val
 12  	
 13  	    return total_sum
(Pdb) unt
> e:\semester 3\python practical\extra\sum.py(13)sum_of_list()
-> return total_sum
(Pdb) p total_sum
48
(Pdb) w
  <string>(1)<module>()
  c:\python39\lib\idlelib\run.py(156)main()
-> ret = method(*args, **kwargs)
  c:\python39\lib\idlelib\run.py(559)runcode()
-> exec(code, self.locals)
  e:\semester 3\python practical\extra\sum.py(15)<module>()
-> sum_val = sum_of_list()
> e:\semester 3\python practical\extra\sum.py(13)sum_of_list()
-> return total_sum
(Pdb) q
Traceback (most recent call last):
  File "E:/Semester 3/Python practical/Extra/sum.py", line 15, in <module>
    sum_val = sum_of_list()
  File "E:/Semester 3/Python practical/Extra/sum.py", line 13, in sum_of_list
    return total_sum
  File "E:/Semester 3/Python practical/Extra/sum.py", line 13, in sum_of_list
    return total_sum
bdb.BdbQuit
>>> 
= RESTART: E:/Semester 3/Python practical/Extra/printsum.py =
> e:\semester 3\python practical\extra\printsum.py(16)print_sum()
-> print("The sum is", sum_val)
(Pdb) w
  <string>(1)<module>()
  c:\python39\lib\idlelib\run.py(156)main()
-> ret = method(*args, **kwargs)
  c:\python39\lib\idlelib\run.py(559)runcode()
-> exec(code, self.locals)
  e:\semester 3\python practical\extra\printsum.py(19)<module>()
-> calculate_sum()
  e:\semester 3\python practical\extra\printsum.py(11)calculate_sum()
-> print_sum(total_sum)
> e:\semester 3\python practical\extra\printsum.py(16)print_sum()
-> print("The sum is", sum_val)
(Pdb) p sum_val
48
(Pdb) p total_sum
*** NameError: name 'total_sum' is not defined
(Pdb) p sum_val
48
(Pdb) u
> e:\semester 3\python practical\extra\printsum.py(11)calculate_sum()
-> print_sum(total_sum)
(Pdb) p total_sum
48
(Pdb) d
> e:\semester 3\python practical\extra\printsum.py(16)print_sum()
-> print("The sum is", sum_val)
(Pdb) p total_sum
*** NameError: name 'total_sum' is not defined
(Pdb) 