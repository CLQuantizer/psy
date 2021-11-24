function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

function loadSent()
{
    $.ajax({
        url:'/go',
        type: 'POST',
        dataType: 'json',
        success: function(data)
		{
          let s = JSON.parse(data);
          let letters  = s.split('');
          let Length = letters.length;
          let offset = 1000;
          for (let i = 0; i < Length; i++)
		    {
	                let js = JSON.stringify(letters[i]);
	                sleep(1000);
	                $(sent).replaceWith(js)
		    }
		}
	  });
}
loadSent();
