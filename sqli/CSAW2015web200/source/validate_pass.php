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

    //�����������,Ӧ����� $hash==NULL���ж�
    //�����û����������� $hash Ϊ�գ� $pass ����Ҳ��Ϊ�գ����ͨ����֤��
    
    if (strlen($pass) != strlen($hash))
        return False;
	echo $pass."</br>";
	echo $hash."</br>"; 
	
    $index = 0;
    while($hash[$index]){   //�ֽ��ж�  ���ڻ���ʱ���ע��  ����ĳλΪ0 ����㲻������ֱ������ѭ����
        if ($pass[$index] != $hash[$index])
            return false;
        # Protect against brute force attacks
        usleep(300000);  //0.3s
        $index+=1;
    }
    return true;
}
?>
