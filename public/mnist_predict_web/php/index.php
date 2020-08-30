<?php
require_once 'functions.php';
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
    <div class="candiv" id="candiv">
        <canvas id="can" width="150px" height="150px"></canvas>
    </div>
    <br>
    <input type="button" onClick="clearCan();" value="クリア" class="button" data-inline="true" />
    <form id="fm" name="fm" method="post" action="/" style="display: inline;">
        <input type="button" onClick="savePic();" value="予測" class="button" data-inline="true" />
        <input type="hidden" name="imgBase64" id="imgBase64" value="" data-inline="true" />
    </form>
    <br>
    <br>
    <h3>予測結果</h3>
    <?= predict();?>
</body>
</html>
