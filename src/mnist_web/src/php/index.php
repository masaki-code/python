<?php
require_once 'functions.php';

$imgBase64 = imgBase64();
$file_name = save($imgBase64);
$output = predict($file_name);
?>
<!DOCTYPE html>
<html lang="ja">
<head>
<META http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>手書き文字の数字予測</title>
<style type="text/css"></style>
<link rel="stylesheet" href="common.css">
<script type="text/javascript" src="common.js"></script>
</head>
<body onload="mam_draw_init();">
    <h3>手書き文字の数字予測</h3>
    <div style="border: solid 1px #000000; width: 150px;" id="candiv">
        <canvas id="can" width="150px" height="150px"></canvas>
    </div>
    <br>
    <input type="button" onClick="clearCan();" value="クリア" style="width: 100; height: 30;" data-inline="true" />
    <form id="fm" name="fm" method="post" action="/" style="display: inline;">
        <input type="button" onClick="savePic();" value="サーバーへ保存" style="width: 100; height: 30;" data-inline="true" />
        <input type="hidden" name="imgBase64" id="imgBase64" value="" data-inline="true" />
    </form>
    <br>
    <br>
    <?php
    if ($imgBase64 != '') {
        echo ('<div style="border: solid 1px #000000;width: 150px;"><img  src="data:image/png;base64,' . $imgBase64 . '" /></div>');
    }
    ?>
    <br>
    <?php
    if ($output != '') {
        output_predict($output);
    }
    ?>
</body>
</html>
