<?php
require_once 'consts.php';

function predict()
{
    $imgBase64 = '';
    if (isset($_POST['imgBase64'])) {
        $imgBase64 = $_POST['imgBase64'];
    }

    if ($imgBase64 == '' || $imgBase64 == EMPTY_BASE64) {
        return '';
    }

    $file_name = '/home/keras/images/' . date("Ymd_His", time()) . '.png';
    $decode = base64_decode($imgBase64);
    file_put_contents($file_name, $decode);

    $python_bin = '/home/keras/venv/bin/python';
    $python_module = '/home/keras/lib/main.py';
    $command = $python_bin . ' ' . $python_module . ' ' . $file_name . ' 2>&1';
    exec($command, $output);

    $result = '';
    $result .= '<div class="candiv"><img  src="data:image/png;base64,' . $imgBase64 . '" /></div>';
    foreach ($output as $value) {
        $result .= $value . '<br>';
    }
    return $result;
}
?>
