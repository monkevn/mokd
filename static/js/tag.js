$("#topic").dropdown();

function pick_hobby(){
	var value=$(this).text();
	var tag=$('<div class="tagger-tag">'+value+'<span class="remove-tag">×</span></div>');
	var target_parent=$(".input-container");
	target_parent.before(tag);
	$(".remove-tag",tag).on('click',function(){
		var text=$(this).parent().text()
		var value=text.substring(0,text.indexOf('×'));
		console.log(value);
		var tag=$('<li class="topic-pick inline-block">'+value+'</li>');
		tag.on('click',pick_hobby);
		var target_parent=$("#returned_topics ul");
		target_parent.prepend(tag);
		$(this).parent().remove();
	})
	$(this).remove();
}
$("#returned_topics ul li.topic-pick").on('click',pick_hobby);
