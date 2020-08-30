<?php
require_once 'consts.php';

function imgBase64()
{
    if (isset($_POST['imgBase64'])) {
        return $_POST['imgBase64'];
    }
    return '';
}

function save($imgBase64)
{
    if ($imgBase64 == '' || $imgBase64 == EMPTY_BASE64) {
        return '';
    }

    $time = time();
    $date = date("Ymd", $time);
    $file_name = '/home/keras/images/' . $date . '_' . $time . '.png';
    $decode = base64_decode($imgBase64);
    file_put_contents($file_name, $decode);
    return $file_name;
}

function predict($file_name)
{
    if ($file_name == '') {
        return '';
    }
    $command = "/home/keras/venv/bin/python /home/keras/lib/main.py " . $file_name . " 2>&1";
    exec($command, $output);
    return $output;
}

function output_predict($output)
{
    foreach ($output as $value) {
        echo $value . '<br>';
    }
}

?>
