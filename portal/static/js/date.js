
   var timeNode = document.getElementById('time');
   var dateNode = document.getElementById('date');

   function getCurrentTimeString() {
      return new Date().toTimeString().replace(/ .*/, '');
   }

   Data = new Date();
   Year = Data.getFullYear();
   Month = Data.getMonth();
   Day = Data.getDate();

   switch (Month)
    {
      case 0: fMonth=gettext("января"); break;
      case 1: fMonth=gettext("февраля"); break;
      case 2: fMonth=gettext("марта"); break;
      case 3: fMonth=gettext("апреля"); break;
      case 4: fMonth=gettext("мая"); break;
      case 5: fMonth=gettext("июня"); break;
      case 6: fMonth=gettext("июля"); break;
      case 7: fMonth=gettext("августа"); break;
      case 8: fMonth=gettext("сентября"); break;
      case 9: fMonth=gettext("октября"); break;
      case 10: fMonth=gettext("ноября"); break;
      case 11: fMonth=gettext("декабря"); break;
    }

   var date = (Day + " " + fMonth + " " + Year + " года");


   dateNode.innerHTML = date;

   setInterval(
      () => timeNode.innerHTML = getCurrentTimeString(),
      1000
   );

