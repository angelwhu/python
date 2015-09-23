<?

//username = ~~FLAG~~ 
function validate($user, $pass) {
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
}
?>
