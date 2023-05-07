<?php
require('image-gallery-script.php'); 
  if(!empty($fetchImage))
  {
    $sn=1;
    foreach ($fetchImage as $img) {
        
?>
    <div class="column">
    <img src="uploads/
<?php
echo $img['image_name']; 
?>
" style="width:100%" onclick="openModal(); currentSlide(
<?php
echo $sn; 
?>
)" class="hover-shadow cursor">
  </div>
<?php
 $sn++;}
  }else{
    echo "No Image is saved in database";
  }
?>