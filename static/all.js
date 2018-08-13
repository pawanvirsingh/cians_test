	$(document).ready(function(){
    var tg = new Date()
    alert("DSKJKDSJ")
    $.ajax({
      url: "http://localhost:8000/ajaxrequest/",
      method: "GET",
      contentType: "application/json",
      success:function(data, exception, jqXHR)  {
        console.log("JJJJJJJJJJJ")
        // console.log(data["data"])
        // console.log(data)
        // console.log(exception)
        // console.log(jqXHR)
        // console.log(jqXHR.responseText)
        str = ""
        item = ""
        info = "<tr>"
        hm = "<tr><th>First Name</th><th>Mobile</th><th>Email</th><th>Skills</th><th>Experience</th></tr>"
        if (data.data.length==0){
          $('#res').html(hm);
        }
        $.each(data.data, function(i, item) {
          info = info+"<th>"+item["name"]+"</th>"+"<th>"+item["mobile"]+"</th>"+"<th>"+item["skills"]+"</th>"+"<th id='myPassword'>"+item["password"]+"</th>"+"</th>"+"<th>"+item["experience"]+"</th></tr>"
          str = str+item["driver_name"]+"<br>"
          // $('#result1').text(item["driver_name"]);
          $("#res").clear;
          $('#res').html(hm+info);
          });
        }
      });

    //   function mouseoverPass(obj) {
    //   var obj = document.getElementById('myPassword');
    //   obj.type = "text";
    // }
      function loadData(search){
        document.getElementById("res").innerText=""
        $.ajax({
          url: "http://localhost:8000/ajaxrequest/",
          method: "POST",
          cache: false,
          async: true,
          data: JSON.stringify({"key": search}),
          contentType: "application/json",
          success:function(data, exception, jqXHR)  {
            console.log("JJJJJJJJJJJ")
            // console.log(data["data"])
            // console.log(data)
            // console.log(exception)
            // console.log(jqXHR)
            // console.log(jqXHR.responseText)
            str = ""
            item = ""
            info = "<tr>"
            hm = "<tr><th>First Name</th><th>Mobile</th><th>Email</th><th>Skills</th><th>Experience</th></tr>"
            if (data.data.length==0){
              $('#res').html(hm);
            }
            $.each(data.data, function(i, item) {
              info = info+"<th>"+item["name"]+"</th>"+"<th>"+item["mobile"]+"</th>"+"<th>"+item["skills"]+"</th>"+"<th id='myPassword'>"+item["password"]+"</th>"+"</th>"+"<th>"+item["experience"]+"</th></tr>"
              str = str+item["driver_name"]+"<br>"
              // $('#result1').text(item["driver_name"]);
              $("#res").clear;
              $('#res').html(hm+info);
              });
            }
          });
        }
        $('#search_text').on("change paste keyup",function(){
          var t1 = new Date();
          console.log("T1: "+t1)
          // h1 = t1.getHours()
          // console.log(h1)

          // var key = e.keyCode
          // console.log(key)
          // $('#search_text').keypress(function(e){

          // console.log(e.keyCode)
          // console.log(e.which)
          var search = $(this).val();
          // setTimeout(function fun(){console.log(search)}, 2000);
          console.log("Search text : "+search);
          $("#result").text("Enter Key");
          if(search != '' && search.length>0)
          {
           // loadData(search)
           // setTimeout(loadData(search), 5000);
           console.log("TG: "+tg)
           td = t1-tg
           console.log(td)
           // setTimeout(function(){loadData(search)},5000);
           if (td>2000){
            loadData(search); 
           }
           tg = t1
           console.log("TG2: "+tg)
           $("#result").text(search)
          }
          else
          {
           $('#res').html("<tr><th>First Name</th><th>Mobile</th><th>Email</th><th>Skills</th><th>Experience</th></tr>");
          }
        // })
      });

  });




