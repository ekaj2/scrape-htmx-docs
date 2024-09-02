# Active Search

URL: https://htmx.org/examples/active-search/

<h1>Active Search</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This example actively searches a contacts database as the user enters text.

We start with a search input and an empty table:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">h3</span><span>&gt; 
</span><span>  Search Contacts 
</span><span>  &lt;</span><span style="color:#e06c75;">span </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"htmx-indicator"</span><span>&gt; 
</span><span>    &lt;</span><span style="color:#e06c75;">img </span><span style="color:#d19a66;">src</span><span>=</span><span style="color:#98c379;">"/img/bars.svg"</span><span>/&gt; Searching... 
</span><span>   &lt;/</span><span style="color:#e06c75;">span</span><span>&gt; 
</span><span>&lt;/</span><span style="color:#e06c75;">h3</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"form-control" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"search" 
</span><span>       </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"search" </span><span style="color:#d19a66;">placeholder</span><span>=</span><span style="color:#98c379;">"Begin Typing To Search Users..." 
</span><span>       </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/search" 
</span><span>       </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"input changed delay:500ms, search" 
</span><span>       </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#search-results" 
</span><span>       </span><span style="color:#d19a66;">hx-indicator</span><span>=</span><span style="color:#98c379;">".htmx-indicator"</span><span>&gt;
</span><span>
</span><span>&lt;</span><span style="color:#e06c75;">table </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"table"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;First Name&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Last Name&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Email&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">tbody </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"search-results"</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">tbody</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">table</span><span>&gt;
</span></code></pre>The input issues a <code>POST</code> to <code>/search</code> on the <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event"><code>input</code></a> event and sets the body of the table to be the resulting content. Note that the <code>keyup</code> event could be used as well, but would not fire if the user pasted text with their mouse (or any other non-keyboard method).

We add the <code>delay:500ms</code> modifier to the trigger to delay sending the query until the user stops typing.  Additionally,
we add the <code>changed</code> modifier to the trigger to ensure we don’t send new queries when the user doesn’t change the
value of the input (e.g. they hit an arrow key, or pasted the same value).

Since we use a <code>search</code> type input we will get an <code>x</code> in the input field to clear the input.
To make this trigger a new <code>POST</code> we have to specify another trigger. We specify another trigger by using a comma to
separate them. The <code>search</code> trigger will be run when the field is cleared but it also makes it possible to override
the 500 ms <code>input</code> event delay by just pressing enter.

Finally, we show an indicator when the search is in flight with the <code>hx-indicator</code> attribute.

<style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>
    
    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // routes
    init("/init", function(request, params){
      return searchUI();
    });
    
    onPost(/\/search.*/, function(request, params){
        var search = params['search'];
        var contacts = dataStore.findContactsMatching(search);
        return resultsUI(contacts);
      });
      
    // templates
    function searchUI() {
      return `  <h3>
Search Contacts
<span class="htmx-indicator">
<img src="/img/bars.svg"/> Searching...
</span>
</h3>

<input class="form-control" type="search" 
       name="search" placeholder="Begin Typing To Search Users..." 
       hx-post="/search" 
       hx-trigger="input changed delay:500ms, search" 
       hx-target="#search-results" 
       hx-indicator=".htmx-indicator">

<table class="table">
<thead>
<tr>
  <th>First Name</th>
  <th>Last Name</th>
  <th>Email</th>
</tr>
</thead>
<tbody id="search-results">
</tbody>
</table>`;
    }
    
    function resultsUI(contacts){
        var txt = "";
        for (var i = 0; i < contacts.length; i++) {
          var c = contacts[i];
          txt += "<tr><td>" + c.FirstName + "</td><td>" + c.LastName + "</td><td>" + c.Email + "</td></tr>\n";
        }
        return txt;  
    }
    
    //datastore
    
     var dataStore = function(){
          var data = [
            { "FirstName": "Venus", "LastName": "Grimes", "Email": "lectus.rutrum@Duisa.edu", "City": "Ankara" },
            { "FirstName": "Fletcher", "LastName": "Owen", "Email": "metus@Aenean.org", "City": "Niort" },
            { "FirstName": "William", "LastName": "Hale", "Email": "eu.dolor@risusodio.edu", "City": "Te Awamutu" },
            { "FirstName": "TaShya", "LastName": "Cash", "Email": "tincidunt.orci.quis@nuncnullavulputate.co.uk", "City": "Titagarh" },
            { "FirstName": "Kevyn", "LastName": "Hoover", "Email": "tristique.pellentesque.tellus@Cumsociis.co.uk", "City": "Cuenca" },
            { "FirstName": "Jakeem", "LastName": "Walker", "Email": "Morbi.vehicula.Pellentesque@faucibusorci.org", "City": "St. Andrä" },
            { "FirstName": "Malcolm", "LastName": "Trujillo", "Email": "sagittis@velit.edu", "City": "Fort Resolution" },
            { "FirstName": "Wynne", "LastName": "Rice", "Email": "augue.id@felisorciadipiscing.edu", "City": "Kinross" },
            { "FirstName": "Evangeline", "LastName": "Klein", "Email": "adipiscing.lobortis@sem.org", "City": "San Giovanni in Galdo" },
            { "FirstName": "Jennifer", "LastName": "Russell", "Email": "sapien.Aenean.massa@risus.com", "City": "Laives/Leifers" },
            { "FirstName": "Rama", "LastName": "Freeman", "Email": "Proin@quamPellentesquehabitant.net", "City": "Flin Flon" },
            { "FirstName": "Jena", "LastName": "Mathis", "Email": "non.cursus.non@Phaselluselit.com", "City": "Fort Simpson" },
            { "FirstName": "Alexandra", "LastName": "Maynard", "Email": "porta.elit.a@anequeNullam.ca", "City": "Nazilli" },
            { "FirstName": "Tallulah", "LastName": "Haley", "Email": "ligula@id.net", "City": "Bay Roberts" },
            { "FirstName": "Timon", "LastName": "Small", "Email": "velit.Quisque.varius@gravidaPraesent.org", "City": "Girona" },
            { "FirstName": "Randall", "LastName": "Pena", "Email": "facilisis@Donecconsectetuer.edu", "City": "Edam" },
            { "FirstName": "Conan", "LastName": "Vaughan", "Email": "luctus.sit@Classaptenttaciti.edu", "City": "Nadiad" },
            { "FirstName": "Dora", "LastName": "Allen", "Email": "est.arcu.ac@Vestibulumante.co.uk", "City": "Renfrew" },
            { "FirstName": "Aiko", "LastName": "Little", "Email": "quam.dignissim@convallisest.net", "City": "Delitzsch" },
            { "FirstName": "Jessamine", "LastName": "Bauer", "Email": "taciti.sociosqu@nibhvulputatemauris.co.uk", "City": "Offida" },
            { "FirstName": "Gillian", "LastName": "Livingston", "Email": "justo@atiaculisquis.com", "City": "Saskatoon" },
            { "FirstName": "Laith", "LastName": "Nicholson", "Email": "elit.pellentesque.a@diam.org", "City": "Tallahassee" },
            { "FirstName": "Paloma", "LastName": "Alston", "Email": "cursus@metus.org", "City": "Cache Creek" },
            { "FirstName": "Freya", "LastName": "Dunn", "Email": "Vestibulum.accumsan@metus.co.uk", "City": "Heist-aan-Zee" },
            { "FirstName": "Griffin", "LastName": "Rice", "Email": "justo@tortordictumeu.net", "City": "Montpelier" },
            { "FirstName": "Catherine", "LastName": "West", "Email": "malesuada.augue@elementum.com", "City": "Tarnów" },
            { "FirstName": "Jena", "LastName": "Chambers", "Email": "erat.Etiam.vestibulum@quamelementumat.net", "City": "Konya" },
            { "FirstName": "Neil", "LastName": "Rodriguez", "Email": "enim@facilisis.com", "City": "Kraków" },
            { "FirstName": "Freya", "LastName": "Charles", "Email": "metus@nec.net", "City": "Arzano" },
            { "FirstName": "Anastasia", "LastName": "Strong", "Email": "sit@vitae.edu", "City": "Polpenazze del Garda" },
            { "FirstName": "Bell", "LastName": "Simon", "Email": "mollis.nec.cursus@disparturientmontes.ca", "City": "Caxias do Sul" },
            { "FirstName": "Minerva", "LastName": "Allison", "Email": "Donec@nequeIn.edu", "City": "Rio de Janeiro" },
            { "FirstName": "Yoko", "LastName": "Dawson", "Email": "neque.sed@semper.net", "City": "Saint-Remy-Geest" },
            { "FirstName": "Nadine", "LastName": "Justice", "Email": "netus@et.edu", "City": "Calgary" },
            { "FirstName": "Hoyt", "LastName": "Rosa", "Email": "Nullam.ut.nisi@Aliquam.co.uk", "City": "Mold" },
            { "FirstName": "Shafira", "LastName": "Noel", "Email": "tincidunt.nunc@non.edu", "City": "Kitzbühel" },
            { "FirstName": "Jin", "LastName": "Nunez", "Email": "porttitor.tellus.non@venenatisamagna.net", "City": "Dreieich" },
            { "FirstName": "Barbara", "LastName": "Gay", "Email": "est.congue.a@elit.com", "City": "Overland Park" },
            { "FirstName": "Riley", "LastName": "Hammond", "Email": "tempor.diam@sodalesnisi.net", "City": "Smoky Lake" },
            { "FirstName": "Molly", "LastName": "Fulton", "Email": "semper@Naminterdumenim.net", "City": "Montese" },
            { "FirstName": "Dexter", "LastName": "Owen", "Email": "non.ante@odiosagittissemper.ca", "City": "Bousval" },
            { "FirstName": "Kuame", "LastName": "Merritt", "Email": "ornare.placerat.orci@nisinibh.ca", "City": "Solingen" },
            { "FirstName": "Maggie", "LastName": "Delgado", "Email": "Nam.ligula.elit@Cum.org", "City": "Tredegar" },
            { "FirstName": "Hanae", "LastName": "Washington", "Email": "nec.euismod@adipiscingelit.org", "City": "Amersfoort" },
            { "FirstName": "Jonah", "LastName": "Cherry", "Email": "ridiculus.mus.Proin@quispede.edu", "City": "Acciano" },
            { "FirstName": "Cheyenne", "LastName": "Munoz", "Email": "at@molestiesodalesMauris.edu", "City": "Saint-L?onard" },
            { "FirstName": "India", "LastName": "Mack", "Email": "sem.mollis@Inmi.co.uk", "City": "Maryborough" },
            { "FirstName": "Lael", "LastName": "Mcneil", "Email": "porttitor@risusDonecegestas.com", "City": "Livorno" },
            { "FirstName": "Jillian", "LastName": "Mckay", "Email": "vulputate.eu.odio@amagnaLorem.co.uk", "City": "Salvador" },
            { "FirstName": "Shaine", "LastName": "Wright", "Email": "malesuada@pharetraQuisqueac.org", "City": "Newton Abbot" },
            { "FirstName": "Keane", "LastName": "Richmond", "Email": "nostra.per.inceptos@euismodurna.org", "City": "Canterano" },
            { "FirstName": "Samuel", "LastName": "Davis", "Email": "felis@euenim.com", "City": "Peterhead" },
            { "FirstName": "Zelenia", "LastName": "Sheppard", "Email": "Quisque.nonummy@antelectusconvallis.org", "City": "Motta Visconti" },
            { "FirstName": "Giacomo", "LastName": "Cole", "Email": "aliquet.libero@urnaUttincidunt.ca", "City": "Donnas" },
            { "FirstName": "Mason", "LastName": "Hinton", "Email": "est@Nunc.co.uk", "City": "St. Asaph" },
            { "FirstName": "Katelyn", "LastName": "Koch", "Email": "velit.Aliquam@Suspendisse.edu", "City": "Cleveland" },
            { "FirstName": "Olga", "LastName": "Spencer", "Email": "faucibus@Praesenteudui.net", "City": "Karapınar" },
            { "FirstName": "Erasmus", "LastName": "Strong", "Email": "dignissim.lacus@euarcu.net", "City": "Passau" },
            { "FirstName": "Regan", "LastName": "Cline", "Email": "vitae.erat.vel@lacusEtiambibendum.co.uk", "City": "Pergola" },
            { "FirstName": "Stone", "LastName": "Holt", "Email": "eget.mollis.lectus@Aeneanegestas.ca", "City": "Houston" },
            { "FirstName": "Deanna", "LastName": "Branch", "Email": "turpis@estMauris.net", "City": "Olcenengo" },
            { "FirstName": "Rana", "LastName": "Green", "Email": "metus@conguea.edu", "City": "Onze-Lieve-Vrouw-Lombeek" },
            { "FirstName": "Caryn", "LastName": "Henson", "Email": "Donec.sollicitudin.adipiscing@sed.net", "City": "Kington" },
            { "FirstName": "Clarke", "LastName": "Stein", "Email": "nec@mollis.co.uk", "City": "Tenali" },
            { "FirstName": "Kelsie", "LastName": "Porter", "Email": "Cum@gravidaAliquam.com", "City": "İskenderun" },
            { "FirstName": "Cooper", "LastName": "Pugh", "Email": "Quisque.ornare.tortor@dictum.co.uk", "City": "Delhi" },
            { "FirstName": "Paul", "LastName": "Spencer", "Email": "ac@InfaucibusMorbi.com", "City": "Biez" },
            { "FirstName": "Cassady", "LastName": "Farrell", "Email": "Suspendisse.non@venenatisa.net", "City": "New Maryland" },
            { "FirstName": "Sydnee", "LastName": "Velazquez", "Email": "mollis@loremfringillaornare.com", "City": "Strée" },
            { "FirstName": "Felix", "LastName": "Boyle", "Email": "id.libero.Donec@aauctor.org", "City": "Edinburgh" },
            { "FirstName": "Ryder", "LastName": "House", "Email": "molestie@natoquepenatibus.org", "City": "Copertino" },
            { "FirstName": "Hadley", "LastName": "Holcomb", "Email": "penatibus@nisi.ca", "City": "Avadi" },
            { "FirstName": "Marsden", "LastName": "Nunez", "Email": "Nulla.eget.metus@facilisisvitaeorci.org", "City": "New Galloway" },
            { "FirstName": "Alana", "LastName": "Powell", "Email": "non.lobortis.quis@interdumfeugiatSed.net", "City": "Pitt Meadows" },
            { "FirstName": "Dennis", "LastName": "Wyatt", "Email": "Morbi.non@nibhQuisquenonummy.ca", "City": "Wrexham" },
            { "FirstName": "Karleigh", "LastName": "Walton", "Email": "nascetur.ridiculus@quamdignissimpharetra.com", "City": "Diksmuide" },
            { "FirstName": "Brielle", "LastName": "Donovan", "Email": "placerat@at.edu", "City": "Kolmont" },
            { "FirstName": "Donna", "LastName": "Dickerson", "Email": "lacus.pede.sagittis@lacusvestibulum.com", "City": "Vallepietra" },
            { "FirstName": "Eagan", "LastName": "Pate", "Email": "est.Nunc@cursusNunc.ca", "City": "Durness" },
            { "FirstName": "Carlos", "LastName": "Ramsey", "Email": "est.ac.facilisis@duinec.co.uk", "City": "Tiruvottiyur" },
            { "FirstName": "Regan", "LastName": "Murphy", "Email": "lectus.Cum@aptent.com", "City": "Candidoni" },
            { "FirstName": "Claudia", "LastName": "Spence", "Email": "Nunc.lectus.pede@aceleifend.co.uk", "City": "Augusta" },
            { "FirstName": "Genevieve", "LastName": "Parker", "Email": "ultrices@inaliquetlobortis.net", "City": "Forbach" },
            { "FirstName": "Marshall", "LastName": "Allison", "Email": "erat.semper.rutrum@odio.org", "City": "Landau" },
            { "FirstName": "Reuben", "LastName": "Davis", "Email": "Donec@auctorodio.edu", "City": "Schönebeck" },
            { "FirstName": "Ralph", "LastName": "Doyle", "Email": "pede.Suspendisse.dui@Curabitur.org", "City": "Linkebeek" },
            { "FirstName": "Constance", "LastName": "Gilliam", "Email": "mollis@Nulla.edu", "City": "Enterprise" },
            { "FirstName": "Serina", "LastName": "Jacobson", "Email": "dictum.augue@ipsum.net", "City": "Hérouville-Saint-Clair" },
            { "FirstName": "Charity", "LastName": "Byrd", "Email": "convallis.ante.lectus@scelerisquemollisPhasellus.co.uk", "City": "Brussegem" },
            { "FirstName": "Hyatt", "LastName": "Bird", "Email": "enim.Nunc.ut@nonmagnaNam.com", "City": "Gdynia" },
            { "FirstName": "Brent", "LastName": "Dunn", "Email": "ac.sem@nuncid.com", "City": "Hay-on-Wye" },
            { "FirstName": "Casey", "LastName": "Bonner", "Email": "id@ornareelitelit.edu", "City": "Kearny" },
            { "FirstName": "Hakeem", "LastName": "Gill", "Email": "dis@nonummyipsumnon.org", "City": "Portico e San Benedetto" },
            { "FirstName": "Stewart", "LastName": "Meadows", "Email": "Nunc.pulvinar.arcu@convallisdolorQuisque.net", "City": "Dignano" },
            { "FirstName": "Nomlanga", "LastName": "Wooten", "Email": "inceptos@turpisegestas.ca", "City": "Troon" },
            { "FirstName": "Sebastian", "LastName": "Watts", "Email": "Sed.diam.lorem@lorem.co.uk", "City": "Palermo" },
            { "FirstName": "Chelsea", "LastName": "Larsen", "Email": "ligula@Nam.net", "City": "Poole" },
            { "FirstName": "Cameron", "LastName": "Humphrey", "Email": "placerat@id.org", "City": "Manfredonia" },
            { "FirstName": "Juliet", "LastName": "Bush", "Email": "consectetuer.euismod@vitaeeratVivamus.co.uk", "City": "Lavacherie" },
            { "FirstName": "Caryn", "LastName": "Hooper", "Email": "eu.enim.Etiam@ridiculus.org", "City": "Amelia" }
          ];
          return {
            findContactsMatching : function(str) {
              var result = [];
              var s = str.toLowerCase();
              for (var i = 0; i < data.length; i++) {
                var c = data[i];
                if(c['FirstName'].toLowerCase().indexOf(s) >= 0 || c['LastName'].toLowerCase().indexOf(s) >= 0 || c['Email'].toLowerCase().indexOf(s) >= 0) {
                  result.push(c)
                }
              }
              return result;
            }
          }
        }()
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Lazy Loading

URL: https://htmx.org/examples/lazy-load/

<h1>Lazy Loading</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This example shows how to lazily load an element on a page.  We start with an initial
state that looks like this:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/graph" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"load"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">img </span><span style="color:#d19a66;">alt</span><span>=</span><span style="color:#98c379;">"Result loading..." </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"htmx-indicator" </span><span style="color:#d19a66;">width</span><span>=</span><span style="color:#98c379;">"150" </span><span style="color:#d19a66;">src</span><span>=</span><span style="color:#98c379;">"/img/bars.svg"</span><span>/&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>Which shows a progress indicator as we are loading the graph.  The graph is then
loaded and faded gently into view via a settling CSS transition:

<pre data-lang="css" style="background-color:#1f2329;color:#abb2bf;" class="language-css "><code class="language-css" data-lang="css"><span style="color:#d19a66;">.htmx-settling </span><span style="color:#e06c75;">img </span><span>{
</span><span>  opacity: </span><span style="color:#d19a66;">0</span><span>;
</span><span>}
</span><span style="color:#e06c75;">img </span><span>{
</span><span> transition: opacity </span><span style="color:#d19a66;">300ms </span><span>ease-in;
</span><span>}
</span></code></pre><style>
.htmx-settling img {
  opacity: 0;
}
img {
 transition: opacity 300ms ease-in;
}
</style><style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>
    server.autoRespondAfter = 2000; // longer response for more drama

    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // routes
    init("/demo", function(request, params){
      return lazyTemplate();
    });

    onGet("/graph", function(request, params){
      return "<img alt='Tokyo Climate' src='/img/tokyo.png'>";
    });

    // templates
    function lazyTemplate(page) {
      return `<div hx-get="/graph" hx-trigger="load">
  <img alt="Result loading..." class="htmx-indicator" width="150" src="/img/bars.svg"/>
</div>`;
    }
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Click To Edit

URL: https://htmx.org/examples/click-to-edit/

<h1>Click to Edit</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>The click to edit pattern provides a way to offer inline editing of all or part of a record without a page refresh.

- This pattern starts with a UI that shows the details of a contact.  The div has a button that will get the editing UI for the contact from <code>/contact/1/edit</code>

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"this" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">div</span><span>&gt;&lt;</span><span style="color:#e06c75;">label</span><span>&gt;First Name&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;: Joe&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">div</span><span>&gt;&lt;</span><span style="color:#e06c75;">label</span><span>&gt;Last Name&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;: Blow&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">div</span><span>&gt;&lt;</span><span style="color:#e06c75;">label</span><span>&gt;Email&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;: joe@blow.com&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/contact/1/edit" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary"</span><span>&gt;
</span><span>    Click To Edit
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>- This returns a form that can be used to edit the contact

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-put</span><span>=</span><span style="color:#98c379;">"/contact/1" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"this" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">label</span><span>&gt;First Name&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"firstName" </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">"Joe"</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"form-group"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">label</span><span>&gt;Last Name&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"lastName" </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">"Blow"</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"form-group"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">label</span><span>&gt;Email Address&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">"joe@blow.com"</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn"</span><span>&gt;Submit&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/contact/1"</span><span>&gt;Cancel&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>- The form issues a <code>PUT</code> back to <code>/contact/1</code>, following the usual REST-ful pattern.

<style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>
    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // data
    var contact = {
        "firstName" : "Joe",
        "lastName" : "Blow",
        "email" : "joe@blow.com"
    };

    // routes
    init("/contact/1", function(request){
        return displayTemplate(contact);
    });

    onGet("/contact/1/edit", function(request){
        return formTemplate(contact);
    });

    onPut("/contact/1", function (req, params) {
        contact.firstName = params['firstName'];
        contact.lastName = params['lastName'];
        contact.email = params['email'];
        return displayTemplate(contact);
    });

    // templates
    function formTemplate(contact) {
return `<form hx-put="/contact/1" hx-target="this" hx-swap="outerHTML">
  <div>
    <label for="firstName">First Name</label>
    <input autofocus type="text" id="firstName" name="firstName" value="${contact.firstName}">
  </div>
  <div class="form-group">
    <label for="lastName">Last Name</label>
    <input type="text" id="lastName" name="lastName" value="${contact.lastName}">
  </div>
  <div class="form-group">
    <label for="email">Email Address</label>
    <input type="email" id="email" name="email" value="${contact.email}">
  </div>
  <button class="btn primary" type="submit">Submit</button>
  <button class="btn danger" hx-get="/contact/1">Cancel</button>
</form>`
    }

    function displayTemplate(contact) {
        return `<div hx-target="this" hx-swap="outerHTML">
    <div><label>First Name</label>: ${contact.firstName}</div>
    <div><label>Last Name</label>: ${contact.lastName}</div>
    <div><label>Email Address</label>: ${contact.email}</div>
    <button hx-get="/contact/1/edit" class="btn primary">
    Click To Edit
    </button>
</div>`;
    }
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Click To Load

URL: https://htmx.org/examples/click-to-load/

<h1>Click to Load</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This example shows how to implement click-to-load the next page in a table of data.  The crux of the demo is
the final row:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">tr </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"replaceMe"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">td </span><span style="color:#d19a66;">colspan</span><span>=</span><span style="color:#98c379;">"3"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">'btn primary' </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/contacts/?page=2"
</span><span>                        </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#replaceMe"
</span><span>                        </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML"</span><span>&gt;
</span><span>         Load More Agents... &lt;</span><span style="color:#e06c75;">img </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"htmx-indicator" </span><span style="color:#d19a66;">src</span><span>=</span><span style="color:#98c379;">"/img/bars.svg"</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span></code></pre>This row contains a button that will replace the entire row with the next page of
results (which will contain a button to load the <em>next</em> page of results).  And so on.

<style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>
    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // data
    var dataStore = function(){
      var contactId = 9;
      function generateContact() {
        contactId++;
        var idHash = "";
        var possible = "ABCDEFG0123456789";
        for( var i=0; i < 15; i++ ) idHash += possible.charAt(Math.floor(Math.random() * possible.length));
        return { name: "Agent Smith", email: "void" + contactId + "@null.org", id: idHash }
      }
      return {
        contactsForPage : function(page) {
          var vals = [];
          for( var i=0; i < 10; i++ ){
            vals.push(generateContact());
          }
          return vals;
        }
      }
    }()

    // routes
    init("/demo", function(request, params){
        var contacts = dataStore.contactsForPage(1)
        return tableTemplate(contacts)
    });

    onGet(/\/contacts.*/, function(request, params){
        var page = parseInt(params['page']);
        var contacts = dataStore.contactsForPage(page)
        return rowsTemplate(page, contacts);
    });

    // templates
    function tableTemplate(contacts) {
        return `<table><thead><tr><th>Name</th><th>Email</th><th>ID</th></tr></thead><tbody>
                ${rowsTemplate(1, contacts)}
                </tbody></table>`
    }

    function rowsTemplate(page, contacts) {
      var txt = "";
      for (var i = 0; i < contacts.length; i++) {
        var c = contacts[i];
        txt += `<tr><td>${c.name}</td><td>${c.email}</td><td>${c.id}</td></tr>\n`;
      }
      txt += loadMoreRow(page);
      return txt;
    }

    function loadMoreRow(page) {
      return `<tr id="replaceMe">
  <td colspan="3">
    <center>
      <button class='btn primary' hx-get="/contacts/?page=${page + 1}"
                       hx-target="#replaceMe"
                       hx-swap="outerHTML">
         Load More Agents... <img class="htmx-indicator" src="/img/bars.svg">
       </button>
    </center>
  </td>
</tr>`;
    }
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Inline Validation

URL: https://htmx.org/examples/inline-validation/

<h1>Inline Validation</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This example shows how to do inline field validation, in this case of an email address.  To do this
we need to create a form with an input that <code>POST</code>s back to the server with the value to be validated
and updates the DOM with the validation results.

We start with this form:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">h3</span><span>&gt;Signup Form&lt;/</span><span style="color:#e06c75;">h3</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/contact"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"this" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">label</span><span>&gt;Email Address&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/contact/email" </span><span style="color:#d19a66;">hx-indicator</span><span>=</span><span style="color:#98c379;">"#ind"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">img </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"ind" </span><span style="color:#d19a66;">src</span><span>=</span><span style="color:#98c379;">"/img/bars.svg" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"htmx-indicator"</span><span>/&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"form-group"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">label</span><span>&gt;First Name&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"form-control" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"firstName"</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"form-group"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">label</span><span>&gt;Last Name&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"form-control" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"lastName"</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary"</span><span>&gt;Submit&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>Note that the first div in the form has set itself as the target of the request and specified the <code>outerHTML</code>
swap strategy, so it will be replaced entirely by the response.  The input then specifies that it will
<code>POST</code> to <code>/contact/email</code> for validation, when the <code>changed</code> event occurs (this is the default for inputs).
It also specifies an indicator for the request.

When a request occurs, it will return a partial to replace the outer div.  It might look like this:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"this" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"error"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">label</span><span>&gt;Email Address&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/contact/email" </span><span style="color:#d19a66;">hx-indicator</span><span>=</span><span style="color:#98c379;">"#ind" </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">"test@foo.com"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">img </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"ind" </span><span style="color:#d19a66;">src</span><span>=</span><span style="color:#98c379;">"/img/bars.svg" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"htmx-indicator"</span><span>/&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">'error-message'</span><span>&gt;That email is already taken.  Please enter another email.&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>Note that this div is annotated with the <code>error</code> class and includes an error message element.

This form can be lightly styled with this CSS:

<pre data-lang="css" style="background-color:#1f2329;color:#abb2bf;" class="language-css "><code class="language-css" data-lang="css"><span>  </span><span style="color:#d19a66;">.error-message </span><span>{
</span><span>    color:red;
</span><span>  }
</span><span>  </span><span style="color:#d19a66;">.error </span><span style="color:#e06c75;">input </span><span>{
</span><span>      box-shadow: </span><span style="color:#d19a66;">0 0 3px </span><span style="color:#56b6c2;">#CC0000</span><span>;
</span><span>   }
</span><span>  </span><span style="color:#d19a66;">.valid </span><span style="color:#e06c75;">input </span><span>{
</span><span>      box-shadow: </span><span style="color:#d19a66;">0 0 3px </span><span style="color:#56b6c2;">#36cc00</span><span>;
</span><span>   }
</span></code></pre>To give better visual feedback.

Below is a working demo of this example.  The only email that will be accepted is <code>test@test.com</code>.

<style>
  .error-message {
    color:red;
  }
  .error input {
      box-shadow: 0 0 3px #CC0000;
   }
  .valid input {
      box-shadow: 0 0 3px #36cc00;
   }
</style><style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>

    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // routes
    init("/demo", function(request, params){
      return demoTemplate();
    });

    onPost("/contact", function(request, params){
      return formTemplate();
    });

    onPost(/\/contact\/email.*/, function(request, params){
        var email = params['email'];
        if(!/\S+@\S+\.\S+/.test(email)) {
          return emailInputTemplate(email, "Please enter a valid email address");
        } else if(email != "test@test.com") {
          return emailInputTemplate(email, "That email is already taken.  Please enter another email.");
        } else {
          return emailInputTemplate(email);
        }
     });

    // templates
    function demoTemplate() {

        return `### Signup FormEnter an email into the input below and on tab out it will be validated.  Only "test@test.com" will pass.

 ` + formTemplate();
    }

    function formTemplate() {
      return `<form hx-post="/contact">
  <div hx-target="this" hx-swap="outerHTML">
    <label for="email">Email Address</label>
    <input name="email" id="email" hx-post="/contact/email" hx-indicator="#ind">
    <img id="ind" src="/img/bars.svg" class="htmx-indicator"/>
  </div>
  <div class="form-group">
    <label for="firstName">First Name</label>
    <input type="text" class="form-control" name="firstName" id="firstName">
  </div>
  <div class="form-group">
    <label for="lastName">Last Name</label>
    <input type="text" class="form-control" name="lastName" id="lastName">
  </div>
  <button type='submit' class="btn primary" disabled>Submit</button>
</form>`;
    }

        function emailInputTemplate(val, errorMsg) {
            return `<div hx-target="this" hx-swap="outerHTML" class="${errorMsg ? "error" : "valid"}">
  <label>Email Address</label>
  <input name="email" hx-post="/contact/email" hx-indicator="#ind" value="${val}" aria-invalid="${!!errorMsg}">
  <img id="ind" src="/img/bars.svg" class="htmx-indicator"/>
  ${errorMsg ? (`<div class='error-message' >${errorMsg}</div>`) : ""}
</div>`;
        }
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Edit Row

URL: https://htmx.org/examples/edit-row/

<h1>Edit Row</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This example shows how to implement editable rows.  First let’s look at the table body:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">table </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"table delete-row-example"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Name&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Email&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">tbody </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"closest tr" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML"</span><span>&gt;
</span><span>    ...
</span><span>  &lt;/</span><span style="color:#e06c75;">tbody</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">table</span><span>&gt;
</span></code></pre>This will tell the requests from within the table to target the closest enclosing row that the request is triggered
on and to replace the entire row.

Here is the HTML for a row:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">td</span><span>&gt;${contact.name}&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">td</span><span>&gt;${contact.email}&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn danger"
</span><span>                </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/contact/${contact.id}/edit"
</span><span>                </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"edit"
</span><span>                </span><span style="color:#d19a66;">onClick</span><span>=</span><span style="color:#98c379;">"let editing = document.querySelector('.editing')
</span><span style="color:#98c379;">                         if(editing) {
</span><span style="color:#98c379;">                           Swal.fire({title: 'Already Editing',
</span><span style="color:#98c379;">                                      showCancelButton: true,
</span><span style="color:#98c379;">                                      confirmButtonText: 'Yep, Edit This Row!',
</span><span style="color:#98c379;">                                      text:'Hey!  You are already editing a row!  Do you want to cancel that edit and continue?'})
</span><span style="color:#98c379;">                           .then((result) =&gt; {
</span><span style="color:#98c379;">                                if(result.isConfirmed) {
</span><span style="color:#98c379;">                                   htmx.trigger(editing, 'cancel')
</span><span style="color:#98c379;">                                   htmx.trigger(this, 'edit')
</span><span style="color:#98c379;">                                }
</span><span style="color:#98c379;">                            })
</span><span style="color:#98c379;">                         } else {
</span><span style="color:#98c379;">                            htmx.trigger(this, 'edit')
</span><span style="color:#98c379;">                         }"</span><span>&gt;
</span><span>          Edit
</span><span>        &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>      &lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span></code></pre>Here we are getting a bit fancy and only allowing one row at a time to be edited, using some JavaScript.
We check to see if there is a row with the <code>.editing</code> class on it and confirm that the user wants to edit this row
and dismiss the other one.  If so, we send a cancel event to the other row so it will issue a request to go back to
its initial state.

We then trigger the <code>edit</code> event on the current element, which triggers the htmx request to get the editable version
of the row.

Note that if you didn’t care if a user was editing multiple rows, you could omit the hyperscript and custom <code>hx-trigger</code>,
and just let the normal click handling work with htmx.  You could also implement mutual exclusivity by simply targeting the
entire table when the Edit button was clicked.  Here we wanted to show how to integrate htmx and JavaScript to solve
the problem and narrow down the server interactions a bit, plus we get to use a nice SweetAlert confirm dialog.

Finally, here is what the row looks like when the data is being edited:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">tr </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">'cancel' </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">'editing' </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/contact/${contact.id}"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">td</span><span>&gt;&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">'name' </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'${contact.name}'</span><span>&gt;&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">td</span><span>&gt;&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">'email' </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'${contact.email}'</span><span>&gt;&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn danger" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/contact/${contact.id}"</span><span>&gt;
</span><span>      Cancel
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn danger" </span><span style="color:#d19a66;">hx-put</span><span>=</span><span style="color:#98c379;">"/contact/${contact.id}" </span><span style="color:#d19a66;">hx-include</span><span>=</span><span style="color:#98c379;">"closest tr"</span><span>&gt;
</span><span>      Save
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span></code></pre>Here we have a few things going on:  First off the row itself can respond to the <code>cancel</code> event, which will bring
back the read-only version of the row.  There is a cancel button that allows
cancelling the current edit.  Finally, there is a save button that issues a <code>PUT</code> to update the contact.  Note that
there is an <a href="https://htmx.org/attributes/hx-include/"><code>hx-include</code></a> that includes all the inputs in the closest row.  Tables rows are
notoriously difficult to use with forms due to HTML constraints (you can’t put a <code>form</code> directly inside a <code>tr</code>) so
this makes things a bit nicer to deal with.

<style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script><script>
    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // data
    var contacts = [
      {
        name: "Joe Smith",
        email: "joe@smith.org",
        status: "Active",
        id: 0
      },
      {
        name: "Angie MacDowell",
        email: "angie@macdowell.org",
        status: "Active",
        id: 1
      },
      {
        name: "Fuqua Tarkenton",
        email: "fuqua@tarkenton.org",
        status: "Active",
        id: 2
      },
      {
        name: "Kim Yee",
        email: "kim@yee.org",
        status: "Inactive",
        id: 3
      },
    ];

    // routes
    init("/demo", function(request, params){
      return tableTemplate(contacts);
    });

    onGet(/\/contact\/\d+/, function(request, params){
      var id = parseInt(request.url.split("/")[2]); // get the contact
      var contact = contacts[id];
      console.log(request, id, contact)
      if(request.url.endsWith("/edit")) {
        return editTemplate(contacts[id])
      } else {
        return rowTemplate(contacts[id])
      }
    });

    onPut(/\/contact\/\d+/, function(request, params){
      var id = parseInt(request.url.split("/")[2]); // get the contact
      contact = contacts[id]
      contact.name = params['name'];
      contact.email = params['email'];
      return rowTemplate(contact);
    });

    // templates
    function rowTemplate(contact) {
      return `<tr>
      <td>${contact.name}</td>
      <td>${contact.email}</td>
      <td>
        <button class="btn danger"
                hx-get="/contact/${contact.id}/edit"
                hx-trigger="edit"
                onClick="let editing = document.querySelector('.editing')
                         if(editing) {
                           Swal.fire({title: 'Already Editing',
                                      showCancelButton: true,
                                      confirmButtonText: 'Yep, Edit This Row!',
                                      text:'Hey!  You are already editing a row!  Do you want to cancel that edit and continue?'})
                           .then((result) => {
                                if(result.isConfirmed) {
                                   htmx.trigger(editing, 'cancel')
                                   htmx.trigger(this, 'edit')
                                }
                            })
                         } else {
                            htmx.trigger(this, 'edit')
                         }">
          Edit
        </button>
      </td>
    </tr>`;
    }

    function editTemplate(contact) {
      return `<tr hx-trigger='cancel' class='editing' hx-get="/contact/${contact.id}">
      <td><input name='name' value='${contact.name}'</td>
      <td><input name='email' value='${contact.email}'</td>
      <td>
        <button class="btn danger" hx-get="/contact/${contact.id}">
          Cancel
        </button>
        <button class="btn danger" hx-put="/contact/${contact.id}" hx-include="closest tr">
          Save
        </button>
      </td>
    </tr>`;
    }

    function tableTemplate(contacts) {
      var rows = "";

      for (var i = 0; i < contacts.length; i++) {
        rows += rowTemplate(contacts[i], i, "");
      }

      return `
<table class="table delete-row-example">
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th></th>
    </tr>
  </thead>
  <tbody hx-target="closest tr" hx-swap="outerHTML">
    ${rows}
  </tbody>
</table>`;
    }
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Bulk Update

URL: https://htmx.org/examples/bulk-update/

<h1>Bulk Update</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This demo shows how to implement a common pattern where rows are selected and then bulk updated.  This is
accomplished by putting a form around a table, with checkboxes in the table, and then including the checked
values in the form submission (<code>POST</code> request):

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"checked-contacts"
</span><span>      </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/users"
</span><span>      </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML settle:3s"
</span><span>      </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#toast"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">table</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Name&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Email&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Active&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>      &lt;/</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">tbody </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"tbody"</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>          &lt;</span><span style="color:#e06c75;">td</span><span>&gt;Joe Smith&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>          &lt;</span><span style="color:#e06c75;">td</span><span>&gt;joe@smith.org&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>          &lt;</span><span style="color:#e06c75;">td</span><span>&gt;&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"checkbox" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"active:joe@smith.org"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>        &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>        ...
</span><span>      &lt;/</span><span style="color:#e06c75;">tbody</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">table</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"submit" </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">"Bulk Update" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">span </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"toast"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">span</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>The server will bulk-update the statuses based on the values of the checkboxes.
We respond with a small toast message about the update to inform the user, and
use ARIA to politely announce the update for accessibility.

<pre data-lang="css" style="background-color:#1f2329;color:#abb2bf;" class="language-css "><code class="language-css" data-lang="css"><span style="color:#d19a66;">#toast.htmx-settling </span><span>{
</span><span>  opacity: </span><span style="color:#d19a66;">100</span><span>;
</span><span>}
</span><span>
</span><span style="color:#d19a66;">#toast </span><span>{
</span><span>  background: </span><span style="color:#56b6c2;">#E1F0DA</span><span>;
</span><span>  opacity: </span><span style="color:#d19a66;">0</span><span>;
</span><span>  transition: opacity </span><span style="color:#d19a66;">3s </span><span>ease-out;
</span><span>}
</span></code></pre>The cool thing is that, because HTML form inputs already manage their own state,
we don’t need to re-render any part of the users table. The active users are
already checked and the inactive ones unchecked!

You can see a working example of this code below.

<style scoped="">
#toast.htmx-settling {
  opacity: 100;
}

#toast {
  background: #E1F0DA;
  opacity: 0;
  transition: opacity 3s ease-out;
}
</style><style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>
    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    const dataStore = (() => {
      const data = {
        "joe@smith.org": {name: 'Joe Smith', status: 'Active'},
        "angie@macdowell.org": {name: 'Angie MacDowell', status: 'Active'},
        "fuqua@tarkenton.org": {name: 'Fuqua Tarkenton', status: 'Active'},
        "kim@yee.org": {name: 'Kim Yee', status: 'Inactive'},
      };

      return {
        all() {
          return data;
        },

        activate(email) {
          if (data[email].status === 'Active') {
            return 0;
          } else {
            data[email].status = 'Active';
            return 1;
          }
        },

        deactivate(email) {
          if (data[email].status === 'Inactive') {
            return 0;
          } else {
            data[email].status = 'Inactive';
            return 1;
          }
        },
      };
    })();

    // routes
    init("/demo", function(request){
        return displayUI(dataStore.all());
    });

    /*
    Params look like:
    {"active:joe@smith.org":"on","active:angie@macdowell.org":"on","active:fuqua@tarkenton.org":"on"}
    */
    onPost("/users", function (req, params) {
      const actives = {};
      let activated = 0;
      let deactivated = 0;

      // Build a set of active users for efficient lookup
      for (const param of Object.keys(params)) {
        const nameEmail = param.split(':');
        if (nameEmail[0] === 'active') {
          actives[nameEmail[1]] = true;
        }
      }

      // Activate or deactivate users based on the lookup
      for (const email of Object.keys(dataStore.all())) {
        if (actives[email]) {
          activated += dataStore.activate(email);
        } else {
          deactivated += dataStore.deactivate(email);
        }
      }

      return `<span id="toast" aria-live="polite">Activated ${activated} and deactivated ${deactivated} users</span>`;
    });

    // templates
    function displayUI(contacts) {
      return `### Select Rows And Activate Or Deactivate Below
               <form
                id="checked-contacts"
                hx-post="/users"
                hx-swap="outerHTML settle:3s"
                hx-target="#toast"
              >
                <table>
                  <thead>
                  <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Active</th>
                  </tr>
                  </thead>
                  <tbody id="tbody">
                    ${displayTable(contacts)}
                  </tbody>
                </table>
                <input type="submit" value="Bulk Update" class="btn primary">
                <span id="toast"></span>
              </form>
              <br>`;
    }

    function displayTable(contacts) {
      var txt = "";

      for (email of Object.keys(contacts)) {
        txt += `
<tr>
  <td>${contacts[email].name}</td>
  <td>${email}</td>
  <td>
    <input
      type="checkbox"
      name="active:${email}"
      ${contacts[email].status === 'Active' ? 'checked' : ''}>
  </td>
</tr>
`;
      }

      return txt;
    }
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Delete Row

URL: https://htmx.org/examples/delete-row/

<h1>Delete Row</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This example shows how to implement a delete button that removes a table row upon completion.  First let’s look at the
table body:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">table </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"table delete-row-example"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Name&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Email&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Status&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">tbody </span><span style="color:#d19a66;">hx-confirm</span><span>=</span><span style="color:#98c379;">"Are you sure?" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"closest tr" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML swap:1s"</span><span>&gt;
</span><span>    ...
</span><span>  &lt;/</span><span style="color:#e06c75;">tbody</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">table</span><span>&gt;
</span></code></pre>The table body has a <a href="https://htmx.org/attributes/hx-confirm/"><code>hx-confirm</code></a> attribute to confirm the delete action.  It also
set the target to be the <code>closest tr</code> that is, the closest table row, for all the buttons (<a href="https://htmx.org/attributes/hx-target/"><code>hx-target</code></a>
is inherited from parents in the DOM.)  The swap specification in <a href="https://htmx.org/attributes/hx-swap/"><code>hx-swap</code></a> says to swap the
entire target out and to wait 1 second after receiving a response.  This last bit is so that we can use the following
CSS:

<pre data-lang="css" style="background-color:#1f2329;color:#abb2bf;" class="language-css "><code class="language-css" data-lang="css"><span style="color:#e06c75;">tr</span><span style="color:#d19a66;">.htmx-swapping </span><span style="color:#e06c75;">td </span><span>{
</span><span>  opacity: </span><span style="color:#d19a66;">0</span><span>;
</span><span>  transition: opacity </span><span style="color:#d19a66;">1s </span><span>ease-out;
</span><span>}
</span></code></pre>To fade the row out before it is swapped/removed.

Each row has a button with a <a href="https://htmx.org/attributes/hx-delete/"><code>hx-delete</code></a> attribute containing the url on which to issue a <code>DELETE</code>
request to delete the row from the server. This request responds with a <code>200</code> status code and empty content, indicating that the
row should be replaced with nothing.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">td</span><span>&gt;Angie MacDowell&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">td</span><span>&gt;angie@macdowell.org&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">td</span><span>&gt;Active&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn danger" </span><span style="color:#d19a66;">hx-delete</span><span>=</span><span style="color:#98c379;">"/contact/1"</span><span>&gt;
</span><span>      Delete
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span></code></pre><style>
tr.htmx-swapping td {
  opacity: 0;
  transition: opacity 1s ease-out;
}
</style><style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>
    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // data
    var contacts = [
      {
        name: "Joe Smith",
        email: "joe@smith.org",
        status: "Active",
      },
      {
        name: "Angie MacDowell",
        email: "angie@macdowell.org",
        status: "Active",
      },
      {
        name: "Fuqua Tarkenton",
        email: "fuqua@tarkenton.org",
        status: "Active",
      },
      {
        name: "Kim Yee",
        email: "kim@yee.org",
        status: "Inactive",
      },
    ];

    // routes
    init("/demo", function(request, params){
      return tableTemplate(contacts);
    });

    onDelete(/\/contact\/\d+/, function(request, params){
      return "";
    });

    // templates
    function rowTemplate(contact, i) {
      return `<tr>
      <td>${contact["name"]}</td>
      <td>${contact["email"]}</td>
      <td>${contact["status"]}</td>
      <td>
        <button class="btn danger" hx-delete="/contact/${i}">
          Delete
        </button>
      </td>
    </tr>`;
    }

    function tableTemplate(contacts) {
      var rows = "";

      for (var i = 0; i < contacts.length; i++) {
        rows += rowTemplate(contacts[i], i, "");
      }

      return `
<table class="table delete-row-example">
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Status</th>
      <th></th>
    </tr>
  </thead>
  <tbody hx-confirm="Are you sure?" hx-target="closest tr" hx-swap="outerHTML swap:1s">
    ${rows}
  </tbody>
</table>`;
    }

</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Web Components

URL: https://htmx.org/examples/web-components/

<h1>Web Components</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This example shows how to integrate HTMX with web components, allowing it to be used inside of shadow DOM.

By default, HTMX doesn’t know anything about your web components, and won’t see anything inside their shadow
DOM. Because of this, you’ll need to manually tell HTMX about your component’s shadow DOM by using
<a rel="noopener" target="_blank" href="https://htmx.org/api/#process"><code>htmx.process</code></a>.

<pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span style="color:#e06c75;">customElements</span><span>.</span><span style="color:#61afef;">define</span><span>(</span><span style="color:#98c379;">'my-component'</span><span>, </span><span style="color:#c678dd;">class </span><span style="color:#e5c07b;">MyComponent </span><span style="color:#c678dd;">extends </span><span style="color:#e5c07b;">HTMLElement </span><span>{
</span><span>  </span><span style="font-style:italic;color:#848da1;">// This method runs when your custom element is added to the page
</span><span>  </span><span style="color:#61afef;">connectedCallback</span><span>() {
</span><span>    </span><span style="color:#c678dd;">const </span><span style="color:#e06c75;">root </span><span>= </span><span style="color:#e06c75;">this</span><span>.</span><span style="color:#61afef;">attachShadow</span><span>({ mode: </span><span style="color:#98c379;">'closed' </span><span>})
</span><span>    root.</span><span style="color:#e06c75;">innerHTML </span><span>= </span><span style="color:#98c379;">`
</span><span style="color:#98c379;">      &lt;button hx-get="/my-component-clicked" hx-target="next div"&gt;Click me!&lt;/button&gt;
</span><span style="color:#98c379;">      &lt;div&gt;&lt;/div&gt;
</span><span style="color:#98c379;">    `
</span><span>    </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">process</span><span>(root) </span><span style="font-style:italic;color:#848da1;">// Tell HTMX about this component's shadow DOM
</span><span>  }
</span><span>})
</span></code></pre>Once you’ve told HTMX about your component’s shadow DOM, most things should work as expected. However, note
that selectors such as in <code>hx-target</code> will only see elements inside the same shadow DOM - if you need to
access things outside of your web components, you can use one of the following options:

- <code>host</code>: Selects the element hosting the current shadow DOM
- <code>global</code>: If used as a prefix, selects from the main document instead of the current shadow DOM

The same principles generally apply to web components that don’t use shadow DOM as well; while selectors
won’t be encapsulated like with shadow DOM, you’ll still have to point HTMX to your component’s content by
calling <code>htmx.process</code>.

<style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>
  //=========================================================================
  // Fake Server Side Code
  //=========================================================================

  // data
  let timesClicked = 0

  customElements.define('my-component', class MyComponent extends HTMLElement {
    // This method runs when your custom element is added to the page
    connectedCallback() {
      const root = this.attachShadow({ mode: 'closed' })
      root.innerHTML = `
        <button hx-get="/my-component-clicked" hx-target="next div">Click me!</button>
        <div></div>
      `
      htmx.process(root) // Tell HTMX about this component's shadow DOM
    }
  })

  // routes
  init('/demo', function() {
    return `<my-component></my-component>`
  })

  onGet('/my-component-clicked', function() {
    return `Clicked ${++timesClicked} time${timesClicked > 1 ? 's' : ''}!

`
  })
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Updating Other Content

URL: https://htmx.org/examples/update-other-content/

<h1>Updating Other Content</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>A question that often comes up when people are first working with htmx is:

<blockquote>
“I need to update other content on the screen.  How do I do this?”


</blockquote>There are multiple ways to do so, and in this example we will walk you through some of them.

We’ll use the following basic UI to discuss this concept: a simple table of contacts, and a form below it
to add new contacts to the table using <a href="https://htmx.org/attributes/hx-post/">hx-post</a>.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">h2</span><span>&gt;Contacts&lt;/</span><span style="color:#e06c75;">h2</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">table </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"table"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Name&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Email&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">tbody </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"contacts-table"</span><span>&gt;
</span><span>    ...
</span><span>  &lt;/</span><span style="color:#e06c75;">tbody</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">table</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">h2</span><span>&gt;Add A Contact&lt;/</span><span style="color:#e06c75;">h2</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/contacts"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    Name
</span><span>        &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"name" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text"</span><span>&gt;  
</span><span>  &lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    Email
</span><span>        &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"email"</span><span>&gt;  
</span><span>  &lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>The problem here is that when you submit a new contact in the form, you want the contact table above to refresh and
include the contact that was just added by the form.

What solutions do we have?

<h2 id="expand"><a class="zola-anchor" href="#expand" aria-label="Anchor link for: expand">#</a>Solution 1: Expand the Target</h2>The easiest solution here is to “expand the target” of the form to enclose both the table <em>and</em> the form.  For example,
you could wrap the whole thing in a <code>div</code> and then target that <code>div</code> in the form:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"table-and-form"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">h2</span><span>&gt;Contacts&lt;/</span><span style="color:#e06c75;">h2</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">table </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"table"</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>          &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Name&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>          &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Email&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>          &lt;</span><span style="color:#e06c75;">th</span><span>&gt;&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>        &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>      &lt;/</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">tbody </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"contacts-table"</span><span>&gt;
</span><span>        ...
</span><span>      &lt;/</span><span style="color:#e06c75;">tbody</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">table</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">h2</span><span>&gt;Add A Contact&lt;/</span><span style="color:#e06c75;">h2</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/contacts" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#table-and-form"</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>        Name
</span><span>            &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"name" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text"</span><span>&gt;  
</span><span>      &lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>        Email
</span><span>            &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"email"</span><span>&gt;  
</span><span>      &lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>Note that we are targeting the enclosing div using the <a href="https://htmx.org/attributes/hx-target/">hx-target</a> attribute.  You would need
to render both the table and the form in the response to the <code>POST</code> to <code>/contacts</code>.

This is a simple and reliable approach, although it might not feel particularly elegant.

<h2 id="oob"><a class="zola-anchor" href="#oob" aria-label="Anchor link for: oob">#</a>Solution 2: Out of Band Responses</h2>A more sophisticated approach to this problem would use <a href="https://htmx.org/attributes/hx-swap-oob/">out of band swaps</a> to swap in
updated content to the DOM.

Using this approach, the HTML doesn’t need to change from the original setup at all:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">h2</span><span>&gt;Contacts&lt;/</span><span style="color:#e06c75;">h2</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">table </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"table"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Name&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Email&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">tbody </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"contacts-table"</span><span>&gt;
</span><span>    ...
</span><span>  &lt;/</span><span style="color:#e06c75;">tbody</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">table</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">h2</span><span>&gt;Add A Contact&lt;/</span><span style="color:#e06c75;">h2</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/contacts"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    Name
</span><span>        &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"name" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text"</span><span>&gt;  
</span><span>  &lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    Email
</span><span>        &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"email"</span><span>&gt;  
</span><span>  &lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>Instead of modifying something on the front end, in your response to the <code>POST</code> to <code>/contacts</code> you would include some additional content:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">tbody </span><span style="color:#d19a66;">hx-swap-oob</span><span>=</span><span style="color:#98c379;">"beforeend:#contacts-table"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">td</span><span>&gt;Joe Smith&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">td</span><span>&gt;joe@smith.com&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">tbody</span><span>&gt;
</span><span>
</span><span>&lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>  Name
</span><span>      &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"name" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text"</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>  Email
</span><span>      &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"email"</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span></code></pre>This content uses the <a href="https://htmx.org/attributes/hx-swap-oob/">hx-swap-oob</a> attribute to append itself to the <code>#contacts-table</code>, updating
the table after a contact is added successfully.

<h2 id="events"><a class="zola-anchor" href="#events" aria-label="Anchor link for: events">#</a>Solution 3: Triggering Events</h2>An even more sophisticated approach would be to trigger a client side event when a successful contact is created and
then listen for that event on the table, causing the table to refresh.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">h2</span><span>&gt;Contacts&lt;/</span><span style="color:#e06c75;">h2</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">table </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"table"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Name&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Email&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">tbody </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"contacts-table" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/contacts/table" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"newContact from:body"</span><span>&gt;
</span><span>    ...
</span><span>  &lt;/</span><span style="color:#e06c75;">tbody</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">table</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">h2</span><span>&gt;Add A Contact&lt;/</span><span style="color:#e06c75;">h2</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/contacts"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    Name
</span><span>        &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"name" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text"</span><span>&gt;  
</span><span>  &lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    Email
</span><span>        &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"email"</span><span>&gt;  
</span><span>  &lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>We have added a new end-point <code>/contacts/table</code> that re-renders the contacts table.  Our trigger for this request
is a custom event, <code>newContact</code>.  We listen for this event on the <code>body</code> because when it
is triggered by the response to the form, it will end up hitting the body due to event bubbling.

When a successful contact creation occurs during a POST to <code>/contacts</code>, the response includes
an <a href="https://htmx.org/headers/hx-trigger/">HX-Trigger</a> response header that looks like this:

<pre data-lang="txt" style="background-color:#1f2329;color:#abb2bf;" class="language-txt "><code class="language-txt" data-lang="txt"><span>HX-Trigger:newContact
</span></code></pre>This will trigger the table to issue a <code>GET</code> to <code>/contacts/table</code> and this will render the newly added contact row<br>
(in addition to the rest of the table.)

Very clean, event driven programming!

<h2 id="path-deps"><a class="zola-anchor" href="#path-deps" aria-label="Anchor link for: path-deps">#</a>Solution 4: Using the Path Dependencies Extension</h2>A final approach is to use REST-ful path dependencies to refresh the table.  Intercooler.js, the predecessor
to htmx, had <a rel="noopener" target="_blank" href="https://intercoolerjs.org/docs.html#dependencies">path-based dependencies</a> integrated into the
library.

htmx dropped this as a core feature, but supports an extension, <a rel="noopener" target="_blank" href="https://github.com/bigskysoftware/htmx-extensions/blob/main/src/path-deps/README.md">path deps</a>, that gives you
similar functionality.

Updating our example to use the extension would involve loading the extension javascript and then
annotating our HTML like so:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">h2</span><span>&gt;Contacts&lt;/</span><span style="color:#e06c75;">h2</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">table </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"table"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Name&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;Email&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">th</span><span>&gt;&lt;/</span><span style="color:#e06c75;">th</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">thead</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">tbody </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"contacts-table" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/contacts/table" </span><span style="color:#d19a66;">hx-ext</span><span>=</span><span style="color:#98c379;">"path-deps"  </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"path-deps" </span><span style="color:#d19a66;">path-deps</span><span>=</span><span style="color:#98c379;">"/contacts"</span><span>&gt;
</span><span>    ...
</span><span>  &lt;/</span><span style="color:#e06c75;">tbody</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">table</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">h2</span><span>&gt;Add A Contact&lt;/</span><span style="color:#e06c75;">h2</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/contacts"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    Name
</span><span>        &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"name" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text"</span><span>&gt;  
</span><span>  &lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    Email
</span><span>        &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"email"</span><span>&gt;  
</span><span>  &lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>Now, when the form posts to the <code>/contacts</code> URL, the <code>path-deps</code> extension will detect that and trigger an <code>path-deps</code>
event on the contacts table, therefore triggering a request.

The advantage here is that you don’t need to do anything fancy with response headers.  The downside is that a request
will be issued on every <code>POST</code>, even if a contact was not successfully created.

<h2 id="which-should-i-use"><a class="zola-anchor" href="#which-should-i-use" aria-label="Anchor link for: which-should-i-use">#</a>Which should I use?</h2>Generally I would recommend the first approach, expanding your target, especially if the elements that need to be
updated are reasonably close to one another in the DOM.  It is simple and reliable.

After that, I would say it is a tossup between the custom event and an OOB swap approaches.  I would lean towards the custom event
approach because I like event-oriented systems, but that’s a personal preference.  Which one you choose should be dictated by your
own software engineering tastes and which of the two matches up better with your server side technology of choice.

Finally, the path-deps approach is interesting, and if it fits well with your mental model and overall system architecture,
it can be a fun way to avoid explicit refreshing.  I would look at it last, however, unless the concept really grabs
you.

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Async Authentication

URL: https://htmx.org/examples/async-auth/

<h1>Async Authentication</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This example shows how to implement an an async auth token flow for htmx.

The technique we will use here will take advantage of the fact that you can delay requests
using the <a href="https://htmx.org/events/#htmx:confirm"><code>htmx:confirm</code></a> event.

We first have a button that should not issue a request until an auth token has been retrieved:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"next output"</span><span>&gt;
</span><span>    An htmx-Powered button
</span><span>  &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">output</span><span>&gt;
</span><span>    --
</span><span>  &lt;/</span><span style="color:#e06c75;">output</span><span>&gt;
</span></code></pre>Next we will add some scripting to work with an <code>auth</code> promise (returned by a library):

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">script</span><span>&gt;
</span><span>  </span><span style="font-style:italic;color:#848da1;">// auth is a promise returned by our authentication system
</span><span>
</span><span>  </span><span style="font-style:italic;color:#848da1;">// await the auth token and store it somewhere
</span><span>  </span><span style="color:#c678dd;">let </span><span style="color:#e06c75;">authToken </span><span>= </span><span style="color:#d19a66;">null</span><span>;
</span><span>  </span><span style="color:#e06c75;">auth</span><span>.</span><span style="color:#e06c75;">then</span><span>((token) </span><span style="color:#c678dd;">=&gt; </span><span>{
</span><span>    </span><span style="color:#e06c75;">authToken </span><span>= </span><span style="color:#e06c75;">token
</span><span>  })
</span><span>  
</span><span>  </span><span style="font-style:italic;color:#848da1;">// gate htmx requests on the auth token
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#e06c75;">on</span><span>(</span><span style="color:#98c379;">"htmx:confirm"</span><span>, (e)</span><span style="color:#c678dd;">=&gt; </span><span>{
</span><span>    </span><span style="font-style:italic;color:#848da1;">// if there is no auth token
</span><span>    </span><span style="color:#c678dd;">if</span><span>(</span><span style="color:#e06c75;">authToken </span><span>== </span><span style="color:#d19a66;">null</span><span>) {
</span><span>      </span><span style="font-style:italic;color:#848da1;">// stop the regular request from being issued
</span><span>      </span><span style="color:#e06c75;">e</span><span>.</span><span style="color:#e06c75;">preventDefault</span><span>() 
</span><span>      </span><span style="font-style:italic;color:#848da1;">// only issue it once the auth promise has resolved
</span><span>      </span><span style="color:#e06c75;">auth</span><span>.</span><span style="color:#e06c75;">then</span><span>(() </span><span style="color:#c678dd;">=&gt; </span><span style="color:#e06c75;">e</span><span>.detail.</span><span style="color:#e06c75;">issueRequest</span><span>()) 
</span><span>    }
</span><span>  })
</span><span>
</span><span>  </span><span style="font-style:italic;color:#848da1;">// add the auth token to the request as a header
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#e06c75;">on</span><span>(</span><span style="color:#98c379;">"htmx:configRequest"</span><span>, (e)</span><span style="color:#c678dd;">=&gt; </span><span>{
</span><span>    </span><span style="color:#e06c75;">e</span><span>.detail.headers[</span><span style="color:#98c379;">"AUTH"</span><span>] = </span><span style="color:#e06c75;">authToken
</span><span>  })
</span><span>&lt;/</span><span style="color:#e06c75;">script</span><span>&gt;
</span></code></pre>Here we use a global variable, but you could use <code>localStorage</code> or whatever preferred mechanism
you want to communicate the authentication token to the <code>htmx:configRequest</code> event.

With this code in place, htmx will not issue requests until the <code>auth</code> promise has been resolved.

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Infinite Scroll

URL: https://htmx.org/examples/infinite-scroll/

<h1>Infinite Scroll</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>The infinite scroll pattern provides a way to load content dynamically on user scrolling action.

Let’s focus on the final row (or the last element of your content):

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">tr </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/contacts/?page=2"
</span><span>    </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"revealed"
</span><span>    </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"afterend"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">td</span><span>&gt;Agent Smith&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">td</span><span>&gt;void29@null.org&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">td</span><span>&gt;55F49448C0&lt;/</span><span style="color:#e06c75;">td</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span></code></pre>This last element contains a listener which, when scrolled into view, will trigger a request. The result is then appended after it.
The last element of the results will itself contain the listener to load the <em>next</em> page of results, and so on.

<blockquote>
<code>revealed</code> - triggered when an element is scrolled into the viewport (also useful for lazy-loading). If you are using <code>overflow</code> in css like <code>overflow-y: scroll</code> you should use <code>intersect once</code> instead of <code>revealed</code>.


</blockquote><style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>
    server.autoRespondAfter = 1000; // longer response for more drama

    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // data
    var dataStore = function(){
      var contactId = 9;
      function generateContact() {
        contactId++;
        var idHash = "";
        var possible = "ABCDEFG0123456789";
        for( var i=0; i < 10; i++ ) idHash += possible.charAt(Math.floor(Math.random() * possible.length));
        return { name: "Agent Smith", email: "void" + contactId + "@null.org", id: idHash }
      }
      return {
        contactsForPage : function(page) {
          var vals = [];
          for( var i=0; i < 20; i++ ){
            vals.push(generateContact());
          }
          return vals;
        }
      }
    }()
    
    // routes
    init("/demo", function(request, params){
      var contacts = dataStore.contactsForPage(1)
      return tableTemplate(contacts)
    });
    
    onGet(/\/contacts.*/, function(request, params){
      var page = parseInt(params['page']);
      var contacts = dataStore.contactsForPage(page)
      return rowsTemplate(page, contacts);
    });
    
    // templates
    function tableTemplate(contacts) {
      return `<table hx-indicator=".htmx-indicator"><thead><tr><th>Name</th><th>Email</th><th>ID</th></tr></thead><tbody>
              ${rowsTemplate(1, contacts)}
              </tbody></table><center><img class="htmx-indicator" width="60" src="/img/bars.svg"></center>`
    }

    function rowsTemplate(page, contacts) {
      var txt = "";
      var trigger_attributes = "";

      for (var i = 0; i < contacts.length; i++) {
        var c = contacts[i];

        if (i == (contacts.length - 1)) {
         trigger_attributes = ` hx-get="/contacts/?page=${page + 1}" hx-trigger="revealed" hx-swap="afterend"`
        }

        txt += "<tr" + trigger_attributes +"><td>" + c.name + "</td><td>" + c.email + "</td><td>" + c.id + "</td></tr>\n";
      }
      return txt;
    }
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Drag & Drop / Sortable

URL: https://htmx.org/examples/sortable/

<h1>Sortable</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>In this example we show how to integrate the <a rel="noopener" target="_blank" href="https://sortablejs.github.io/Sortable/">Sortable</a>
javascript library with htmx.

To begin we initialize the <code>.sortable</code> class with the <code>Sortable</code> javascript library:

<pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">onLoad</span><span>(</span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">content</span><span>) {
</span><span>    </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">sortables </span><span>= </span><span style="color:#e06c75;">content</span><span>.</span><span style="color:#56b6c2;">querySelectorAll</span><span>(</span><span style="color:#98c379;">".sortable"</span><span>);
</span><span>    </span><span style="color:#c678dd;">for </span><span>(</span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">i </span><span>= </span><span style="color:#d19a66;">0</span><span>; </span><span style="color:#e06c75;">i </span><span>&lt; </span><span style="color:#e06c75;">sortables</span><span>.length; </span><span style="color:#e06c75;">i</span><span>++) {
</span><span>      </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">sortable </span><span>= </span><span style="color:#e06c75;">sortables</span><span>[</span><span style="color:#e06c75;">i</span><span>];
</span><span>      </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">sortableInstance </span><span>= new Sortable(</span><span style="color:#e06c75;">sortable</span><span>, {
</span><span>          animation: </span><span style="color:#d19a66;">150</span><span>,
</span><span>          ghostClass: </span><span style="color:#98c379;">'blue-background-class'</span><span>,
</span><span>
</span><span>          </span><span style="font-style:italic;color:#848da1;">// Make the `.htmx-indicator` unsortable
</span><span>          filter: </span><span style="color:#98c379;">".htmx-indicator"</span><span>,
</span><span>          </span><span style="color:#61afef;">onMove</span><span>: </span><span style="color:#c678dd;">function </span><span>(</span><span style="color:#e06c75;">evt</span><span>) {
</span><span>            </span><span style="color:#c678dd;">return </span><span style="color:#e06c75;">evt</span><span>.</span><span style="color:#e06c75;">related</span><span>.className.</span><span style="color:#56b6c2;">indexOf</span><span>(</span><span style="color:#98c379;">'htmx-indicator'</span><span>) === -</span><span style="color:#d19a66;">1</span><span>;
</span><span>          },
</span><span>
</span><span>          </span><span style="font-style:italic;color:#848da1;">// Disable sorting on the `end` event
</span><span>          </span><span style="color:#61afef;">onEnd</span><span>: </span><span style="color:#c678dd;">function </span><span>(</span><span style="color:#e06c75;">evt</span><span>) {
</span><span>            </span><span style="color:#e06c75;">this</span><span>.</span><span style="color:#61afef;">option</span><span>(</span><span style="color:#98c379;">"disabled"</span><span>, </span><span style="color:#d19a66;">true</span><span>);
</span><span>          }
</span><span>      });
</span><span>
</span><span>      </span><span style="font-style:italic;color:#848da1;">// Re-enable sorting on the `htmx:afterSwap` event
</span><span>      </span><span style="color:#e06c75;">sortable</span><span>.</span><span style="color:#56b6c2;">addEventListener</span><span>(</span><span style="color:#98c379;">"htmx:afterSwap"</span><span>, </span><span style="color:#c678dd;">function</span><span>() {
</span><span>        </span><span style="color:#e06c75;">sortableInstance</span><span>.</span><span style="color:#61afef;">option</span><span>(</span><span style="color:#98c379;">"disabled"</span><span>, </span><span style="color:#d19a66;">false</span><span>);
</span><span>      });
</span><span>    }
</span><span>})
</span></code></pre>Next, we create a form that has some sortable divs within it, and we trigger an ajax request on the <code>end</code> event, fired
by Sortable.js:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"sortable" </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/items" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"end"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"htmx-indicator"</span><span>&gt;Updating...&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div</span><span>&gt;&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">'hidden' </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">'item' </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'1'</span><span>/&gt;Item 1&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div</span><span>&gt;&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">'hidden' </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">'item' </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'2'</span><span>/&gt;Item 2&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div</span><span>&gt;&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">'hidden' </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">'item' </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'3'</span><span>/&gt;Item 3&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div</span><span>&gt;&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">'hidden' </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">'item' </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'4'</span><span>/&gt;Item 4&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div</span><span>&gt;&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">'hidden' </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">'item' </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'5'</span><span>/&gt;Item 5&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>Note that each div has a hidden input inside of it that specifies the item id for that row.

When the list is reordered via the Sortable.js drag-and-drop, the <code>end</code> event will be fired.  htmx will then post
the item ids in the new order to <code>/items</code>, to be persisted by the server.

That’s it!

<style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script src="https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js"></script><script>

    //=========================================================================
    // Fake Server Side Code
    //=========================================================================
    htmx.onLoad(function(content) {
        var sortables = content.querySelectorAll(".sortable");
        for (var i = 0; i < sortables.length; i++) {
          var sortable = sortables[i];
          var sortableInstance = new Sortable(sortable, {
              animation: 150,
              ghostClass: 'blue-background-class',

              // Make the `.htmx-indicator` unsortable
              filter: ".htmx-indicator",
              onMove: function (evt) {
                return evt.related.className.indexOf('htmx-indicator') === -1;
              },

              // Disable sorting on the `end` event
              onEnd: function (evt) {
                this.option("disabled", true);
              }
          });

          // Re-enable sorting on the `htmx:afterSwap` event
          sortable.addEventListener("htmx:afterSwap", function() {
            sortableInstance.option("disabled", false);
          });
        }
    })
    
    var listItems = [1, 2, 3, 4, 5]
    // routes
    init("/demo", function(request, params){
      return '<form id="example1" class="list-group col sortable" hx-post="/items" hx-trigger="end">' +
      listContents()
      + "\n</form>";
    });
    
    onPost("/items", function (request, params) {
      console.log(params);
      listItems = params.item;
      return listContents();
    });
    
    // templates
    function listContents() {
      return '<div class="htmx-indicator" style="cursor: default">Updating...</div>' + listItems.map(function(val) {
        return `  <div style="border:1px solid #DEDEDE; padding:12px; margin: 8px; width:200px; cursor: grab" ondrag="this.style.cursor = 'grabbing'" ><input type="hidden" name="item" value="` + val + `"/> Item ` + val + `</div>`;
      }).join("\n");
    }

</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Keyboard Shortcuts

URL: https://htmx.org/examples/keyboard-shortcuts/

<h1>Keyboard Shortcuts</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>In this example we show how to create a keyboard shortcut for an action.

We start with a simple button that loads some content from the server:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"click, keyup[altKey&amp;&amp;shiftKey&amp;&amp;key=='D'] from:body"
</span><span>        </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/doit"</span><span>&gt;Do It! (alt-shift-D)&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>Note that the button responds to both the <code>click</code> event (as usual) and also the keyup event when <code>alt-shift-D</code> is pressed.
The <code>from:</code> modifier is used to listen for the keyup event on the <code>body</code> element, thus making it a “global” keyboard
shortcut.

You can trigger the demo below by either clicking on the button, or by hitting alt-shift-D.

You can find out the conditions needed for a given keyboard shortcut here:

<a rel="noopener" target="_blank" href="https://javascript.info/keyboard-events">https://javascript.info/keyboard-events</a>

<style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>

    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // routes
    init("/init", function(request, params){
        return "<button class='btn primary' style='font-size:20pt' hx-trigger='click, keyup[altKey&&shiftKey&&key==\"D\"] from:body'" +
                      " hx-post='/doit'>Do It! (alt-shift-D) </button>";
    });

    onPost("/doit", function (request, params) {
        return "Did it!";
    });

</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Tabs (Using JavaScript)

URL: https://htmx.org/examples/tabs-javascript/

<h1>Tabs (Using JavaScript)</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This example shows how to load tab contents using htmx, and to select the “active” tab using Javascript.  This reduces
some duplication by offloading some of the work of re-rendering the tab HTML from your application server to your
clients’ browsers.

You may also consider <a href="https://htmx.org/examples/tabs-hateoas/">a more idiomatic approach</a> that follows the principle of <a rel="noopener" target="_blank" href="https://en.wikipedia.org/wiki/HATEOAS">Hypertext As The Engine Of Application State</a>.

<h2 id="example-code"><a class="zola-anchor" href="#example-code" aria-label="Anchor link for: example-code">#</a>Example Code</h2>The HTML below displays a list of tabs, with added HTMX to dynamically load each tab pane from the server.  A simple
JavaScript event handler uses the <a rel="noopener" target="_blank" href="https://hyperscript.org/commands/take/"><code>take</code> function</a> to switch the selected tab
when the content is swapped into the DOM.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"tabs" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#tab-contents" </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"tablist"
</span><span>     </span><span style="color:#d19a66;">hx-on:htmx-after-on-load</span><span>=</span><span style="color:#98c379;">"let currentTab = document.querySelector('[aria-selected=true]');
</span><span style="color:#98c379;">                               currentTab.setAttribute('aria-selected', 'false')
</span><span style="color:#98c379;">                               currentTab.classList.remove('selected')
</span><span style="color:#98c379;">                               let newTab = event.target
</span><span style="color:#98c379;">                               newTab.setAttribute('aria-selected', 'true')
</span><span style="color:#98c379;">                               newTab.classList.add('selected')"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"tab" </span><span style="color:#d19a66;">aria-controls</span><span>=</span><span style="color:#98c379;">"tab-contents" </span><span style="color:#d19a66;">aria-selected</span><span>=</span><span style="color:#98c379;">"true" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/tab1" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"selected"</span><span>&gt;Tab 1&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"tab" </span><span style="color:#d19a66;">aria-controls</span><span>=</span><span style="color:#98c379;">"tab-contents" </span><span style="color:#d19a66;">aria-selected</span><span>=</span><span style="color:#98c379;">"false" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/tab2"</span><span>&gt;Tab 2&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"tab" </span><span style="color:#d19a66;">aria-controls</span><span>=</span><span style="color:#98c379;">"tab-contents" </span><span style="color:#d19a66;">aria-selected</span><span>=</span><span style="color:#98c379;">"false" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/tab3"</span><span>&gt;Tab 3&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"tab-contents" </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"tabpanel" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/tab1" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"load"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><div id="tabs" hx-target="#tab-contents" role="tablist" hx-on:htmx-after-on-load="console.log(event)
                               let currentTab = document.querySelector('[aria-selected=true]');
                                          currentTab.setAttribute('aria-selected', 'false')
                                          currentTab.classList.remove('selected')
                                          let newTab = event.target
                                          newTab.setAttribute('aria-selected', 'true')
                                          newTab.classList.add('selected')">
	<button role="tab" aria-controls="tab-contents" aria-selected="true" hx-get="/tab1" class="selected">Tab 1</button>
	<button role="tab" aria-controls="tab-contents" aria-selected="false" hx-get="/tab2">Tab 2</button>
	<button role="tab" aria-controls="tab-contents" aria-selected="false" hx-get="/tab3">Tab 3</button>
</div><div id="tab-contents" role="tabpanel" hx-get="/tab1" hx-trigger="load"></div><script src="https://unpkg.com/hyperscript.org"></script><script>
	onGet("/tab1", function() {
		return `
			Commodo normcore truffaut VHS duis gluten-free keffiyeh iPhone taxidermy godard ramps anim pour-over.
			Pitchfork vegan mollit umami quinoa aute aliquip kinfolk eiusmod live-edge cardigan ipsum locavore.
			Polaroid duis occaecat narwhal small batch food truck.
			PBR&B venmo shaman small batch you probably haven't heard of them hot chicken readymade.
			Enim tousled cliche woke, typewriter single-origin coffee hella culpa.
			Art party readymade 90's, asymmetrical hell of fingerstache ipsum.


		`});
	onGet("/tab2", function() {
		return `
			Kitsch fanny pack yr, farm-to-table cardigan cillum commodo reprehenderit plaid dolore cronut meditation.
			Tattooed polaroid veniam, anim id cornhole hashtag sed forage.
			Microdosing pug kitsch enim, kombucha pour-over sed irony forage live-edge.
			Vexillologist eu nulla trust fund, street art blue bottle selvage raw denim.
			Dolore nulla do readymade, est subway tile affogato hammock 8-bit.
			Godard elit offal pariatur you probably haven't heard of them post-ironic.
			Prism street art cray salvia.


		`
	});
	onGet("/tab3", function() {
		return `
			Aute chia marfa echo park tote bag hammock mollit artisan listicle direct trade.
			Raw denim flexitarian eu godard etsy.
			Poke tbh la croix put a bird on it fixie polaroid aute cred air plant four loko gastropub swag non brunch.
			Iceland fanny pack tumeric magna activated charcoal bitters palo santo laboris quis consectetur cupidatat portland aliquip venmo.


		`
	});

</script><style>

	#demo-canvas {
		display:none;
	}

	#tabs {
	}

	#tabs > button {
		border: none;
		display: inline-block;
		padding: 5px 10px;
		cursor:pointer;
		background-color: transparent;
		border: solid 3px rgba(0,0,0,0);
		border-bottom: solid 3px #eee;
	}

	#tabs > button:hover {
		color: var(--midBlue);
	}

	#tabs > button.selected {
		border: solid 3px var(--midBlue);
	}

	#tab-contents {
		padding:10px;
	}
</style><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Confirm

URL: https://htmx.org/examples/confirm/

<h1>A Customized Confirmation UI</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>htmx supports the <a href="https://htmx.org/attributes/hx-confirm/"><code>hx-confirm</code></a> attribute to provide a simple mechanism for confirming a user
action.  This uses the default <code>confirm()</code> function in javascript which, while trusty, may not be consistent with your
applications UX.

In this example we will see how to use <a rel="noopener" target="_blank" href="https://sweetalert2.github.io">sweetalert2</a>  to implement a custom confirmation dialog. Below are two
examples, one using a click+custom event method, and one using the built-in <code>hx-confirm</code> attribute and
the <a href="https://htmx.org/events/#htmx:confirm"><code>htmx:confirm</code></a> event.

<h2 id="using-on-click-custom-event"><a class="zola-anchor" href="#using-on-click-custom-event" aria-label="Anchor link for: using-on-click-custom-event">#</a>Using on click+custom event</h2><pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">script </span><span style="color:#d19a66;">src</span><span>=</span><span style="color:#98c379;">"https://cdn.jsdelivr.net/npm/sweetalert2@11"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">script</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/confirmed" 
</span><span>        </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">'confirmed'
</span><span>        </span><span style="color:#d19a66;">onClick</span><span>=</span><span style="color:#98c379;">"Swal.fire({title: 'Confirm', text:'Do you want to continue?'}).then((result)=&gt;{
</span><span style="color:#98c379;">            if(result.isConfirmed){
</span><span style="color:#98c379;">              htmx.trigger(this, 'confirmed');  
</span><span style="color:#98c379;">            } 
</span><span style="color:#98c379;">        })"</span><span>&gt;
</span><span>  Click Me
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>Here we use javascript to show a Sweet Alert 2 on a click, asking for confirmation.  If the user confirms
the dialog, we then trigger the request by triggering the custom “confirmed” event
which is then picked up by <code>hx-trigger</code>.

<h2 id="vanilla-js-hx-confirm"><a class="zola-anchor" href="#vanilla-js-hx-confirm" aria-label="Anchor link for: vanilla-js-hx-confirm">#</a>Vanilla JS, hx-confirm</h2><pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">script </span><span style="color:#d19a66;">src</span><span>=</span><span style="color:#98c379;">"https://cdn.jsdelivr.net/npm/sweetalert2@11"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">script</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">script</span><span>&gt;
</span><span>  document.</span><span style="color:#e06c75;">addEventListener</span><span>(</span><span style="color:#98c379;">"htmx:confirm"</span><span>, </span><span style="color:#c678dd;">function</span><span>(e) {
</span><span>    </span><span style="color:#e06c75;">e</span><span>.</span><span style="color:#e06c75;">preventDefault</span><span>()
</span><span>    </span><span style="color:#e5c07b;">Swal</span><span>.</span><span style="color:#e06c75;">fire</span><span>({
</span><span>      title: </span><span style="color:#98c379;">"Proceed?"</span><span>,
</span><span>      text: </span><span style="color:#98c379;">`I ask you... </span><span>${</span><span style="color:#e06c75;">e</span><span>.detail.question}</span><span style="color:#98c379;">`
</span><span>    }).</span><span style="color:#e06c75;">then</span><span>(</span><span style="color:#c678dd;">function</span><span>(result) {
</span><span>      </span><span style="color:#c678dd;">if</span><span>(</span><span style="color:#e06c75;">result</span><span>.isConfirmed) </span><span style="color:#e06c75;">e</span><span>.detail.</span><span style="color:#e06c75;">issueRequest</span><span>(</span><span style="color:#d19a66;">true</span><span>) </span><span style="font-style:italic;color:#848da1;">// use true to skip window.confirm
</span><span>    })
</span><span>  })
</span><span>&lt;/</span><span style="color:#e06c75;">script</span><span>&gt;
</span><span>  
</span><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/confirmed" </span><span style="color:#d19a66;">hx-confirm</span><span>=</span><span style="color:#98c379;">"Some confirm text here"</span><span>&gt;
</span><span>  Click Me
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>We add some javascript to invoke Sweet Alert 2 on a click, asking for confirmation.  If the user confirms
the dialog, we trigger the request by calling the <code>issueRequest</code> method. We pass <code>skipConfirmation=true</code> as argument to skip <code>window.confirm</code>.

This allows to use <code>hx-confirm</code>’s value in the prompt which is convenient
when the question depends on the element e.g. a django list:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>{% for client in clients %}
</span><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/delete/{{client.pk}}" </span><span style="color:#d19a66;">hx-confirm</span><span>=</span><span style="color:#98c379;">"Delete {{client.name}}??"</span><span>&gt;Delete&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>{% endfor %}
</span></code></pre><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Tabs (Using HATEOAS)

URL: https://htmx.org/examples/tabs-hateoas/

<h1>Tabs (Using HATEOAS)</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This example shows how easy it is to implement tabs using htmx.  Following the principle of <a rel="noopener" target="_blank" href="https://en.wikipedia.org/wiki/HATEOAS">Hypertext As The Engine Of Application State</a>, the selected tab is a part of the application state.  Therefore, to display and select tabs in your application, simply include the tab markup in the returned HTML.  If this does not suit your application server design, you can also use a little bit of <a href="https://htmx.org/examples/tabs-javascript/">JavaScript to select tabs instead</a>.

<h2 id="example-code-main-page"><a class="zola-anchor" href="#example-code-main-page" aria-label="Anchor link for: example-code-main-page">#</a>Example Code (Main Page)</h2>The main page simply includes the following HTML to load the initial tab into the DOM.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"tabs" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/tab1" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"load delay:100ms" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#tabs" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"innerHTML"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h2 id="example-code-each-tab"><a class="zola-anchor" href="#example-code-each-tab" aria-label="Anchor link for: example-code-each-tab">#</a>Example Code (Each Tab)</h2>Subsequent tab pages display all tabs and highlight the selected one accordingly.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"tab-list" </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"tablist"</span><span>&gt;
</span><span>	&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/tab1" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"selected" </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"tab" </span><span style="color:#d19a66;">aria-selected</span><span>=</span><span style="color:#98c379;">"true" </span><span style="color:#d19a66;">aria-controls</span><span>=</span><span style="color:#98c379;">"tab-content"</span><span>&gt;Tab 1&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>	&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/tab2" </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"tab" </span><span style="color:#d19a66;">aria-selected</span><span>=</span><span style="color:#98c379;">"false" </span><span style="color:#d19a66;">aria-controls</span><span>=</span><span style="color:#98c379;">"tab-content"</span><span>&gt;Tab 2&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>	&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/tab3" </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"tab" </span><span style="color:#d19a66;">aria-selected</span><span>=</span><span style="color:#98c379;">"false" </span><span style="color:#d19a66;">aria-controls</span><span>=</span><span style="color:#98c379;">"tab-content"</span><span>&gt;Tab 3&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"tab-content" </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"tabpanel" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"tab-content"</span><span>&gt;
</span><span>	Commodo normcore truffaut VHS duis gluten-free keffiyeh iPhone taxidermy godard ramps anim pour-over.
</span><span>	Pitchfork vegan mollit umami quinoa aute aliquip kinfolk eiusmod live-edge cardigan ipsum locavore.
</span><span>	Polaroid duis occaecat narwhal small batch food truck.
</span><span>	PBR&amp;B venmo shaman small batch you probably haven't heard of them hot chicken readymade.
</span><span>	Enim tousled cliche woke, typewriter single-origin coffee hella culpa.
</span><span>	Art party readymade 90's, asymmetrical hell of fingerstache ipsum.
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><div id="tabs" hx-target="this" hx-swap="innerHTML">
		<div class="tab-list" role="tablist">
			<button hx-get="/tab1" class="selected" role="tab" aria-selected="true" aria-controls="tab-content">Tab 1</button>
			<button hx-get="/tab2" role="tab" aria-selected="false" aria-controls="tab-content">Tab 2</button>
			<button hx-get="/tab3" role="tab" aria-selected="false" aria-controls="tab-content">Tab 3</button>
		</div>
		<div id="tab-content" role="tabpanel" class="tab-content">
			Commodo normcore truffaut VHS duis gluten-free keffiyeh iPhone taxidermy godard ramps anim pour-over.
			Pitchfork vegan mollit umami quinoa aute aliquip kinfolk eiusmod live-edge cardigan ipsum locavore.
			Polaroid duis occaecat narwhal small batch food truck.
			PBR&amp;B venmo shaman small batch you probably haven't heard of them hot chicken readymade.
			Enim tousled cliche woke, typewriter single-origin coffee hella culpa.
			Art party readymade 90's, asymmetrical hell of fingerstache ipsum.
		</div>
</div><script>
	onGet("/tab1", function() {
		return `
		<div class="tab-list" role="tablist">
			<button hx-get="/tab1" class="selected" aria-selected="true" autofocus role="tab" aria-controls="tab-content">Tab 1</button>
			<button hx-get="/tab2" role="tab" aria-selected="false" aria-controls="tab-content">Tab 2</button>
			<button hx-get="/tab3" role="tab" aria-selected="false" aria-controls="tab-content">Tab 3</button>
		</div>

		<div id="tab-content" role="tabpanel" class="tab-content">
			Commodo normcore truffaut VHS duis gluten-free keffiyeh iPhone taxidermy godard ramps anim pour-over.
			Pitchfork vegan mollit umami quinoa aute aliquip kinfolk eiusmod live-edge cardigan ipsum locavore.
			Polaroid duis occaecat narwhal small batch food truck.
			PBR&B venmo shaman small batch you probably haven't heard of them hot chicken readymade.
			Enim tousled cliche woke, typewriter single-origin coffee hella culpa.
			Art party readymade 90's, asymmetrical hell of fingerstache ipsum.
		</div>`
	})

	onGet("/tab2", function() {
		return `
		<div class="tab-list" role="tablist">
			<button hx-get="/tab1" role="tab" aria-selected="false" aria-controls="tab-content">Tab 1</button>
			<button hx-get="/tab2" class="selected" aria-selected="true" autofocus role="tab" aria-controls="tab-content">Tab 2</button>
			<button hx-get="/tab3" role="tab" aria-selected="false" aria-controls="tab-content">Tab 3</button>
		</div>

		<div id="tab-content" role="tabpanel" class="tab-content">
			Kitsch fanny pack yr, farm-to-table cardigan cillum commodo reprehenderit plaid dolore cronut meditation.
			Tattooed polaroid veniam, anim id cornhole hashtag sed forage.
			Microdosing pug kitsch enim, kombucha pour-over sed irony forage live-edge.
			Vexillologist eu nulla trust fund, street art blue bottle selvage raw denim.
			Dolore nulla do readymade, est subway tile affogato hammock 8-bit.
			Godard elit offal pariatur you probably haven't heard of them post-ironic.
			Prism street art cray salvia.
		</div>`
	})

	onGet("/tab3", function() {
		return `
		<div class="tab-list" role="tablist">
			<button hx-get="/tab1" role="tab" aria-selected="false" aria-controls="tab-content">Tab 1</button>
			<button hx-get="/tab2" role="tab" aria-selected="false" aria-controls="tab-content">Tab 2</button>
			<button hx-get="/tab3" class="selected" aria-selected="true" autofocus role="tab" aria-controls="tab-content">Tab 3</button>
		</div>

		<div id="tab-content" role="tabpanel" class="tab-content">
			Aute chia marfa echo park tote bag hammock mollit artisan listicle direct trade.
			Raw denim flexitarian eu godard etsy.
			Poke tbh la croix put a bird on it fixie polaroid aute cred air plant four loko gastropub swag non brunch.
			Iceland fanny pack tumeric magna activated charcoal bitters palo santo laboris quis consectetur cupidatat portland aliquip venmo.
		</div>`
	})

</script><style>
	#demo-canvas {
		display:none;
	}

	#tabs > .tab-list button {
		border: none;
		display: inline-block;
		padding: 5px 10px;
		cursor:pointer;
		background-color: transparent;
		color: var(--textColor);
		border: solid 3px rgba(0,0,0,0);
		border-bottom: solid 3px #eee;
	}

	#tabs > .tab-list button:hover {
		color: var(--midBlue);
	}

	#tabs > .tab-list button.selected {
		border: solid 3px var(--midBlue);
	}

	#tabs > .tab-content {
		padding:10px;
		margin-bottom:100px;
	}
</style><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Dialogs - Custom

URL: https://htmx.org/examples/modal-custom/

<h1>Custom Modal Dialogs</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>While htmx works great with dialogs built into CSS frameworks (like <a href="https://htmx.org/examples/modal-bootstrap/">Bootstrap</a> and <a href="https://htmx.org/examples/modal-uikit/">UIKit</a>), htmx also makes
it easy to build modal dialogs from scratch.  Here is a quick example of one way to build them.

Click here to see a demo of the final result:

<button class="btn primary" hx-get="/modal" hx-target="body" hx-swap="beforeend">Open a Modal</button>

<h2 id="high-level-plan"><a class="zola-anchor" href="#high-level-plan" aria-label="Anchor link for: high-level-plan">#</a>High Level Plan</h2>We’re going to make a button that loads remote content from the server, then displays it in a modal dialog.  The modal
content will be added to the end of the <code>&lt;body&gt;</code> element, in a div named <code>#modal</code>.

In this demo we’ll define some nice animations in CSS, and then use some <a rel="noopener" target="_blank" href="https://hyperscript.org">Hyperscript</a> to remove the
modals from the DOM when the user is done.  Hyperscript is <em>not</em> required with htmx, but the two were designed to be used
together and it is much nicer for writing async &amp; event oriented code than JavaScript, which is why we chose it for this
example.

<h2 id="main-page-html"><a class="zola-anchor" href="#main-page-html" aria-label="Anchor link for: main-page-html">#</a>Main Page HTML</h2><pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/modal" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"body" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"beforeend"</span><span>&gt;Open a Modal&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre><h2 id="modal-html-fragment"><a class="zola-anchor" href="#modal-html-fragment" aria-label="Anchor link for: modal-html-fragment">#</a>Modal HTML Fragment</h2><pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"modal" </span><span style="color:#d19a66;">_</span><span>=</span><span style="color:#98c379;">"on closeModal add .closing then wait for animationend then remove me"</span><span>&gt;
</span><span>	&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"modal-underlay" </span><span style="color:#d19a66;">_</span><span>=</span><span style="color:#98c379;">"on click trigger closeModal"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>	&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"modal-content"</span><span>&gt;
</span><span>		&lt;</span><span style="color:#e06c75;">h1</span><span>&gt;Modal Dialog&lt;/</span><span style="color:#e06c75;">h1</span><span>&gt;
</span><span>		This is the modal content.
</span><span>		You can put anything here, like text, or a form, or an image.
</span><span>		&lt;</span><span style="color:#e06c75;">br</span><span>&gt;
</span><span>		&lt;</span><span style="color:#e06c75;">br</span><span>&gt;
</span><span>		&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn danger" </span><span style="color:#d19a66;">_</span><span>=</span><span style="color:#98c379;">"on click trigger closeModal"</span><span>&gt;Close&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>	&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h2 id="custom-stylesheet"><a class="zola-anchor" href="#custom-stylesheet" aria-label="Anchor link for: custom-stylesheet">#</a>Custom Stylesheet</h2><pre data-lang="css" style="background-color:#1f2329;color:#abb2bf;" class="language-css "><code class="language-css" data-lang="css"><span style="font-style:italic;color:#848da1;">/***** MODAL DIALOG ****/
</span><span style="color:#d19a66;">#modal </span><span>{
</span><span>	</span><span style="font-style:italic;color:#848da1;">/* Underlay covers entire screen. */
</span><span>	position: fixed;
</span><span>	top:</span><span style="color:#d19a66;">0px</span><span>;
</span><span>	bottom: </span><span style="color:#d19a66;">0px</span><span>;
</span><span>	left:</span><span style="color:#d19a66;">0px</span><span>;
</span><span>	right:</span><span style="color:#d19a66;">0px</span><span>;
</span><span>	background-color:</span><span style="color:#56b6c2;">rgba</span><span>(</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0.5</span><span>);
</span><span>	z-index:</span><span style="color:#d19a66;">1000</span><span>;
</span><span>
</span><span>	</span><span style="font-style:italic;color:#848da1;">/* Flexbox centers the .modal-content vertically and horizontally */
</span><span>	display:flex;
</span><span>	flex-direction:column;
</span><span>	align-items:center;
</span><span>
</span><span>	</span><span style="font-style:italic;color:#848da1;">/* Animate when opening */
</span><span>	animation-name: fadeIn;
</span><span>	animation-duration:</span><span style="color:#d19a66;">150ms</span><span>;
</span><span>	animation-timing-function: ease;
</span><span>}
</span><span>
</span><span style="color:#d19a66;">#modal </span><span style="color:#c678dd;">&gt; </span><span style="color:#d19a66;">.modal-underlay </span><span>{
</span><span>	</span><span style="font-style:italic;color:#848da1;">/* underlay takes up the entire viewport. This is only
</span><span style="font-style:italic;color:#848da1;">	required if you want to click to dismiss the popup */
</span><span>	position: absolute;
</span><span>	z-index: </span><span style="color:#d19a66;">-1</span><span>;
</span><span>	top:</span><span style="color:#d19a66;">0px</span><span>;
</span><span>	bottom:</span><span style="color:#d19a66;">0px</span><span>;
</span><span>	left: </span><span style="color:#d19a66;">0px</span><span>;
</span><span>	right: </span><span style="color:#d19a66;">0px</span><span>;
</span><span>}
</span><span>
</span><span style="color:#d19a66;">#modal </span><span style="color:#c678dd;">&gt; </span><span style="color:#d19a66;">.modal-content </span><span>{
</span><span>	</span><span style="font-style:italic;color:#848da1;">/* Position visible dialog near the top of the window */
</span><span>	margin-top:</span><span style="color:#d19a66;">10vh</span><span>;
</span><span>
</span><span>	</span><span style="font-style:italic;color:#848da1;">/* Sizing for visible dialog */
</span><span>	width:</span><span style="color:#d19a66;">80%</span><span>;
</span><span>	max-width:</span><span style="color:#d19a66;">600px</span><span>;
</span><span>
</span><span>	</span><span style="font-style:italic;color:#848da1;">/* Display properties for visible dialog*/
</span><span>	border:solid </span><span style="color:#d19a66;">1px </span><span style="color:#56b6c2;">#999</span><span>;
</span><span>	border-radius:</span><span style="color:#d19a66;">8px</span><span>;
</span><span>	box-shadow: </span><span style="color:#d19a66;">0px 0px 20px 0px </span><span style="color:#56b6c2;">rgba</span><span>(</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0.3</span><span>);
</span><span>	background-color:white;
</span><span>	padding:</span><span style="color:#d19a66;">20px</span><span>;
</span><span>
</span><span>	</span><span style="font-style:italic;color:#848da1;">/* Animate when opening */
</span><span>	animation-name:zoomIn;
</span><span>	animation-duration:</span><span style="color:#d19a66;">150ms</span><span>;
</span><span>	animation-timing-function: ease;
</span><span>}
</span><span>
</span><span style="color:#d19a66;">#modal.closing </span><span>{
</span><span>	</span><span style="font-style:italic;color:#848da1;">/* Animate when closing */
</span><span>	animation-name: fadeOut;
</span><span>	animation-duration:</span><span style="color:#d19a66;">150ms</span><span>;
</span><span>	animation-timing-function: ease;
</span><span>}
</span><span>
</span><span style="color:#d19a66;">#modal.closing </span><span style="color:#c678dd;">&gt; </span><span style="color:#d19a66;">.modal-content </span><span>{
</span><span>	</span><span style="font-style:italic;color:#848da1;">/* Animate when closing */
</span><span>	animation-name: zoomOut;
</span><span>	animation-duration:</span><span style="color:#d19a66;">150ms</span><span>;
</span><span>	animation-timing-function: ease;
</span><span>}
</span><span>
</span><span style="color:#c678dd;">@keyframes </span><span>fadeIn {
</span><span>	</span><span style="color:#d19a66;">0% </span><span>{opacity: </span><span style="color:#d19a66;">0</span><span>;}
</span><span>	</span><span style="color:#d19a66;">100% </span><span>{opacity: </span><span style="color:#d19a66;">1</span><span>;}
</span><span>}
</span><span>
</span><span style="color:#c678dd;">@keyframes </span><span>fadeOut {
</span><span>	</span><span style="color:#d19a66;">0% </span><span>{opacity: </span><span style="color:#d19a66;">1</span><span>;}
</span><span>	</span><span style="color:#d19a66;">100% </span><span>{opacity: </span><span style="color:#d19a66;">0</span><span>;}
</span><span>}
</span><span>
</span><span style="color:#c678dd;">@keyframes </span><span>zoomIn {
</span><span>	</span><span style="color:#d19a66;">0% </span><span>{transform: </span><span style="color:#56b6c2;">scale</span><span>(</span><span style="color:#d19a66;">0.9</span><span>);}
</span><span>	</span><span style="color:#d19a66;">100% </span><span>{transform: </span><span style="color:#56b6c2;">scale</span><span>(</span><span style="color:#d19a66;">1</span><span>);}
</span><span>}
</span><span>
</span><span style="color:#c678dd;">@keyframes </span><span>zoomOut {
</span><span>	</span><span style="color:#d19a66;">0% </span><span>{transform: </span><span style="color:#56b6c2;">scale</span><span>(</span><span style="color:#d19a66;">1</span><span>);}
</span><span>	</span><span style="color:#d19a66;">100% </span><span>{transform: </span><span style="color:#56b6c2;">scale</span><span>(</span><span style="color:#d19a66;">0.9</span><span>);}
</span><span>}
</span></code></pre><script src="https://unpkg.com/htmx.org"></script><script src="https://unpkg.com/hyperscript.org"></script><script type="text/javascript">

    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // routes
    init("/modal", function(request){
		return `
		<div id="modal" _="on closeModal add .closing wait for animationend then remove me">
			<div class="modal-underlay" _="on click trigger closeModal"></div>
			<div class="modal-content">
				<h1>Modal Dialog</h1>
				This is the modal content.
				You can put anything here, like text, or a form, or an image.
				<br>
				<br>
				<button class="btn danger" _="on click trigger closeModal">Close</button>
			</div>
		</div>
		`
      });
</script><style>
/***** MODAL DIALOG ****/

#modal {
	/* Underlay covers entire screen. */
	position: fixed;
	top:0px;
	bottom: 0px;
	left:0px;
	right:0px;
	background-color:rgba(0,0,0,0.5);
	z-index:1000;

	/* Flexbox centers the .modal-content vertically and horizontally */
	display:flex;
	flex-direction:column;
	align-items:center;

	/* Animate when opening */
	animation-name: fadeIn;
	animation-duration:150ms;
	animation-timing-function: ease;
}

#modal > .modal-underlay {
	/* underlay takes up the entire viewport. This is only
	required if you want to click to dismiss the popup */
	position: absolute;
	z-index: -1;
	top:0px;
	bottom:0px;
	left: 0px;
	right: 0px;
}

#modal > .modal-content {
	/* Position visible dialog near the top of the window */
	margin-top:10vh;

	/* Sizing for visible dialog */
	width:80%;
	max-width:600px;

	/* Display properties for visible dialog*/
	border:solid 1px #999;
	border-radius:8px;
	box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.3);
	background-color:white;
	padding:20px;

	/* Animate when opening */
	animation-name:zoomIn;
	animation-duration:150ms;
	animation-timing-function: ease;
}

#modal.closing {
	/* Animate when closing */
	animation-name: fadeOut;
	animation-duration:150ms;
	animation-timing-function: ease;
}

#modal.closing > .modal-content {
	/* Animate when closing */
	animation-name: zoomOut;
	animation-duration:150ms;
	animation-timing-function: ease;
}

@keyframes fadeIn {
	0% {opacity: 0;}
	100% {opacity: 1;}
}

@keyframes fadeOut {
	0% {opacity: 1;}
	100% {opacity: 0;}
}

@keyframes zoomIn {
	0% {transform: scale(0.9);}
	100% {transform: scale(1);}
}

@keyframes zoomOut {
	0% {transform: scale(1);}
	100% {transform: scale(0.9);}
}
</style><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Dialogs - UIKit

URL: https://htmx.org/examples/modal-uikit/

<h1>Modal Dialogs with UIKit</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>Many CSS toolkits include styles (and Javascript) for creating modal dialog boxes.
This example shows how to use HTMX to display dynamic dialog using UIKit, and how to
trigger its animation styles with little or no Javascript.

We start with a button that triggers the dialog, along with a DIV at the bottom of your
markup where the dialog will be loaded:

This is an example of using HTMX to remotely load modal dialogs using UIKit.  In this example we will use
<a rel="noopener" target="_blank" href="https://hyperscript.org">Hyperscript</a> to demonstrate how cleanly that scripting language allows you to
glue htmx and other libraries together.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button 
</span><span>	</span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"showButton"
</span><span>	</span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/uikit-modal.html" 
</span><span>	</span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#modals-here" 
</span><span>	</span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"uk-button uk-button-primary" 
</span><span>	</span><span style="color:#d19a66;">_</span><span>=</span><span style="color:#98c379;">"on htmx:afterOnLoad wait 10ms then add .uk-open to #modal"</span><span>&gt;Open Modal&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"modals-here"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This button uses a <code>GET</code> request to <code>/uikit-modal.html</code> when this button is clicked.  The
contents of this file will be added to the DOM underneath the <code>#modals-here</code> DIV.

Rather than using the standard UIKit Javascript library we are using a bit of Hyperscript,
which triggers UIKit’s smooth animations. It is delayed by 10ms so that UIKit’s animations
will run correctly.

Finally, the server responds with a slightly modified version of UIKit’s standard modal

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"modal" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"uk-modal" </span><span style="color:#d19a66;">style</span><span>=</span><span style="color:#98c379;">"</span><span>display:block;</span><span style="color:#98c379;">"</span><span>&gt;
</span><span>	&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"uk-modal-dialog uk-modal-body"</span><span>&gt;
</span><span>		&lt;</span><span style="color:#e06c75;">h2 </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"uk-modal-title"</span><span>&gt;Modal Dialog&lt;/</span><span style="color:#e06c75;">h2</span><span>&gt;
</span><span>		&lt;</span><span style="color:#e06c75;">p</span><span>&gt;This modal dialog was loaded dynamically by HTMX.&lt;/</span><span style="color:#e06c75;">p</span><span>&gt;
</span><span>
</span><span>		&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">_</span><span>=</span><span style="color:#98c379;">"on submit take .uk-open from #modal"</span><span>&gt;
</span><span>			&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"uk-margin"</span><span>&gt;
</span><span>				&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"uk-input" </span><span style="color:#d19a66;">placeholder</span><span>=</span><span style="color:#98c379;">"What is Your Name?"</span><span>&gt;
</span><span>			&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>			&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"button" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"uk-button uk-button-primary"</span><span>&gt;Save Changes&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>			&lt;</span><span style="color:#e06c75;">button 
</span><span>				</span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"cancelButton"
</span><span>				</span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"button" 
</span><span>				</span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"uk-button uk-button-default" 
</span><span>				</span><span style="color:#d19a66;">_</span><span>=</span><span style="color:#98c379;">"on click take .uk-open from #modal wait 200ms then remove #modal"</span><span>&gt;Close&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>		&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span><span>	&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>Hyperscript on the button and the form trigger animations when this dialog is completed
or canceled.  If you didn’t use this Hyperscript, the modals will still work but UIKit’s
fade in animations will not be triggered.

You can, of course, use JavaScript rather than Hyperscript for this work, it’s just a lot more code:

<pre data-lang="javascript" style="background-color:#1f2329;color:#abb2bf;" class="language-javascript "><code class="language-javascript" data-lang="javascript"><span>
</span><span style="font-style:italic;color:#848da1;">// This triggers the fade-in animation when a modal dialog is loaded and displayed
</span><span>window.</span><span style="color:#e06c75;">document</span><span>.</span><span style="color:#56b6c2;">getElementById</span><span>(</span><span style="color:#98c379;">"showButton"</span><span>).</span><span style="color:#56b6c2;">addEventListener</span><span>(</span><span style="color:#98c379;">"htmx:afterOnLoad"</span><span>, </span><span style="color:#c678dd;">function</span><span>() {
</span><span>	</span><span style="color:#56b6c2;">setTimeout</span><span>(</span><span style="color:#c678dd;">function</span><span>(){
</span><span>		window.</span><span style="color:#e06c75;">document</span><span>.</span><span style="color:#56b6c2;">getElementById</span><span>(</span><span style="color:#98c379;">"modal"</span><span>).</span><span style="color:#e06c75;">classList</span><span>.</span><span style="color:#56b6c2;">add</span><span>(</span><span style="color:#98c379;">"uk-open"</span><span>)
</span><span>	}, </span><span style="color:#d19a66;">10</span><span>)
</span><span>})
</span><span>
</span><span>
</span><span style="font-style:italic;color:#848da1;">// This triggers the fade-out animation when the modal is closed.
</span><span>window.</span><span style="color:#e06c75;">document</span><span>.</span><span style="color:#56b6c2;">getElementById</span><span>(</span><span style="color:#98c379;">"cancelButton"</span><span>).</span><span style="color:#56b6c2;">addEventListener</span><span>(</span><span style="color:#98c379;">"click"</span><span>, </span><span style="color:#c678dd;">function</span><span>() {
</span><span>	window.</span><span style="color:#e06c75;">document</span><span>.</span><span style="color:#56b6c2;">getElementById</span><span>(</span><span style="color:#98c379;">"modal"</span><span>).</span><span style="color:#e06c75;">classList</span><span>.</span><span style="color:#56b6c2;">remove</span><span>(</span><span style="color:#98c379;">"uk-open"</span><span>)
</span><span>	</span><span style="color:#56b6c2;">setTimeout</span><span>(</span><span style="color:#c678dd;">function</span><span>(){
</span><span>		window.</span><span style="color:#e06c75;">document</span><span>.</span><span style="color:#56b6c2;">getElementById</span><span>(</span><span style="color:#98c379;">"modals-here"</span><span>).</span><span style="color:#e06c75;">innerHTML </span><span>= </span><span style="color:#98c379;">""
</span><span>		,</span><span style="color:#d19a66;">200
</span><span>	})
</span><span>})
</span></code></pre><div id="modals-here"></div><style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><style>
	@import "https://cdnjs.cloudflare.com/ajax/libs/uikit/3.5.9/css/uikit-core.min.css";
</style><script src="https://unpkg.com/hyperscript.org"></script><script>
    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // routes
    init("/demo", function(request, params) {
		return `
<button 
	class="uk-button uk-button-primary" 
	hx-get="/modal" 
	hx-trigger="click" 
	hx-target="#modals-here"
	_="on htmx:afterOnLoad wait 10ms then add .uk-open to #modal">Show Modal Dialog</button>`
	})
		
	onGet("/modal", function(request, params){
	  return `
<div id="modal" class="uk-modal" style="display:block;">
	<div class="uk-modal-dialog uk-modal-body">
		<h2 class="uk-modal-title">Modal Dialog</h2>
		This modal dialog was loaded dynamically by HTMX.  You can put any server request here and you don't (necessarily) need to use the UIKit Javascript file to make it work



		<form _="on submit take .uk-open from #modal">
			<div class="uk-margin">
				<input class="uk-input" placeholder="What is Your Name?">
			</div>

			<div class="uk-margin">
				<input class="uk-input" placeholder="What is Your Quest?">
			</div>

			<div class="uk-margin">
				<input class="uk-input" placeholder="What is Your Favorite Color?">
			</div>

			<button type="button" class="uk-button uk-button-primary" _="on click call alert('submit to server and close dialog.')">Save Changes</button>
			<button type="button" class="uk-button uk-button-default" _="on click take .uk-open from #modal wait 200ms then remove #modal">Close</button>
		</form>
	</div>
</div>`
});
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Dialogs - Browser

URL: https://htmx.org/examples/dialogs/

<h1>Dialogs</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>Dialogs can be triggered with the <a href="https://htmx.org/attributes/hx-prompt/"><code>hx-prompt</code></a> and <a href="https://htmx.org/attributes/hx-confirm/"><code>hx-confirm</code></a>attributes.  These are triggered by the user interaction that would trigger the AJAX request, but the request is only sent if the dialog is accepted.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary"
</span><span>          </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/submit"
</span><span>          </span><span style="color:#d19a66;">hx-prompt</span><span>=</span><span style="color:#98c379;">"Enter a string"
</span><span>          </span><span style="color:#d19a66;">hx-confirm</span><span>=</span><span style="color:#98c379;">"Are you sure?"
</span><span>          </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#response"</span><span>&gt;
</span><span>    Prompt Submission
</span><span>  &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"response"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>The value provided by the user to the prompt dialog is sent to the server in a <code>HX-Prompt</code> header.  In this case, the server simply echos the user input back.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>User entered &lt;</span><span style="color:#e06c75;">i</span><span>&gt;${response}&lt;/</span><span style="color:#e06c75;">i</span><span>&gt;
</span></code></pre><style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>

    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // routes
    init("/demo", function(request, params){
      return submitButton();
    });

    onPost("/submit", function(request, params){
        var response = request.requestHeaders['HX-Prompt'];
        return promptSubmit(response);
    });

    // templates
    function submitButton() {
      return `<div>
  <button class="btn primary"
          hx-post="/submit"
          hx-prompt="Enter a string"
          hx-confirm="Are you sure?"
          hx-target="#response">
    Prompt Submission
  </button>
  <div id="response"></div>
</div>`;
    }

    function promptSubmit(response) {
        return `User entered <i>${response}</i>`;
    }
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Preserving File Inputs after Form Errors

URL: https://htmx.org/examples/file-upload-input/

<h1>Preserving File Inputs after Form Errors</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>When using server-side error handling and validation with forms that include both primitive values and file inputs, the file input’s value is lost when the form returns with error messages. Consequently, users are required to re-upload the file, resulting in a less user-friendly experience.

To overcome the problem of losing file input value in simple cases, you can adopt the following approach:

Before:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">method</span><span>=</span><span style="color:#98c379;">"POST" </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"binaryForm" </span><span style="color:#d19a66;">enctype</span><span>=</span><span style="color:#98c379;">"multipart/form-data" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#binaryForm"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"file" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"binaryFile"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"submit"</span><span>&gt;Submit&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>After:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">form</span><span>=</span><span style="color:#98c379;">"binaryForm" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"file" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"binaryFile"</span><span>&gt;
</span><span>
</span><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">method</span><span>=</span><span style="color:#98c379;">"POST" </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"binaryForm" </span><span style="color:#d19a66;">enctype</span><span>=</span><span style="color:#98c379;">"multipart/form-data" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#binaryForm"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"submit"</span><span>&gt;Submit&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre><ol>
<li>
Form Restructuring: Move the binary file input outside the main form element in the HTML structure.


</li>
<li>
Using the form Attribute: Enhance the binary file input by adding the form attribute and setting its value to the ID of the main form. This linkage associates the binary file input with the form, even when it resides outside the form element.


</li>
</ol><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# File Upload

URL: https://htmx.org/examples/file-upload/

<h1>File Upload</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>In this example we show how to create a file upload form that will be submitted via ajax, along
with a progress bar.

We will show two different implementation, one in pure javascript (using some utility methods in htmx) and one in <a rel="noopener" target="_blank" href="https://hyperscript.org">hyperscript</a>

First the pure javascript version.

- We have a form of type <code>multipart/form-data</code> so that the file will be properly encoded
- We post the form to <code>/upload</code>
- We have a <code>progress</code> element
- We listen for the <code>htmx:xhr:progress</code> event and update the <code>value</code> attribute of the progress bar based on the <code>loaded</code> and <code>total</code> properties in the event detail.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>    &lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">'form' </span><span style="color:#d19a66;">hx-encoding</span><span>=</span><span style="color:#98c379;">'multipart/form-data' </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">'/upload'</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">'file' </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">'file'</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>            Upload
</span><span>        &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">progress </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">'progress' </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'0' </span><span style="color:#d19a66;">max</span><span>=</span><span style="color:#98c379;">'100'</span><span>&gt;&lt;/</span><span style="color:#e06c75;">progress</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">script</span><span>&gt;
</span><span>        </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#e06c75;">on</span><span>(</span><span style="color:#98c379;">'#form'</span><span>, </span><span style="color:#98c379;">'htmx:xhr:progress'</span><span>, </span><span style="color:#c678dd;">function</span><span>(evt) {
</span><span>          </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#e06c75;">find</span><span>(</span><span style="color:#98c379;">'#progress'</span><span>).</span><span style="color:#e06c75;">setAttribute</span><span>(</span><span style="color:#98c379;">'value'</span><span>, </span><span style="color:#e06c75;">evt</span><span>.detail.loaded/</span><span style="color:#e06c75;">evt</span><span>.detail.total * </span><span style="color:#d19a66;">100</span><span>)
</span><span>        });
</span><span>    &lt;/</span><span style="color:#e06c75;">script</span><span>&gt;
</span></code></pre>The Hyperscript version is very similar, except:

- The script is embedded directly on the form element
- Hyperscript offers nicer syntax (although the htmx API is pretty nice too!)

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>    &lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-encoding</span><span>=</span><span style="color:#98c379;">'multipart/form-data' </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">'/upload'
</span><span>          </span><span style="color:#d19a66;">_</span><span>=</span><span style="color:#98c379;">'on htmx:xhr:progress(loaded, total) set #progress.value to (loaded/total)*100'</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">'file' </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">'file'</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>            Upload
</span><span>        &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">progress </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">'progress' </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'0' </span><span style="color:#d19a66;">max</span><span>=</span><span style="color:#98c379;">'100'</span><span>&gt;&lt;/</span><span style="color:#e06c75;">progress</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>Note that hyperscript allows you to destructure properties from <code>details</code> directly into variables

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Animations

URL: https://htmx.org/examples/animations/

<h1>Animations</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>htmx is designed to allow you to use <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions">CSS transitions</a>
to add smooth animations and transitions to your web page using only CSS and HTML.  Below are a few examples of
various animation techniques.

htmx also allows you to use the new <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API">View Transitions API</a>
for creating animations.

### <a class="zola-anchor" href="#basic" aria-label="Anchor link for: basic">#</a>Basic CSS Animations### <a class="zola-anchor" href="#color-throb" aria-label="Anchor link for: color-throb">#</a>Color ThrobThe simplest animation technique in htmx is to keep the <code>id</code> of an element stable across a content swap.  If the
<code>id</code> of an element is kept stable, htmx will swap it in such a way that CSS transitions can be written between
the old version of the element and the new one.

Consider this div:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span style="color:#d19a66;">.smooth </span><span>{
</span><span>  transition: all </span><span style="color:#d19a66;">1s </span><span>ease-in;
</span><span>}
</span><span>&lt;/</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"color-demo" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"smooth" </span><span style="color:#d19a66;">style</span><span>=</span><span style="color:#98c379;">"</span><span>color:red</span><span style="color:#98c379;">"
</span><span>      </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/colors" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"every 1s"</span><span>&gt;
</span><span>  Color Swap Demo
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>
</span></code></pre>This div will poll every second and will get replaced with new content which changes the <code>color</code> style to a new value
(e.g. <code>blue</code>):

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"color-demo" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"smooth" </span><span style="color:#d19a66;">style</span><span>=</span><span style="color:#98c379;">"</span><span>color:blue</span><span style="color:#98c379;">"
</span><span>      </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/colors" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"every 1s"</span><span>&gt;
</span><span>  Color Swap Demo
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>Because the div has a stable id, <code>color-demo</code>, htmx will structure the swap such that a CSS transition, defined on the
<code>.smooth</code> class, applies to the style update from <code>red</code> to <code>blue</code>, and smoothly transitions between them.

<h4 id="throb-demo"><a class="zola-anchor" href="#throb-demo" aria-label="Anchor link for: throb-demo">#</a>Demo</h4><style>
.smooth {
  transition: all 1s ease-in;
}
</style><div id="color-demo" class="smooth" style="color:red" hx-get="/colors" hx-swap="outerHTML" hx-trigger="every 1s">
  Color Swap Demo
</div><script>
    var colors = ['blue', 'green', 'orange', 'red'];
    onGet("/colors", function () {
      var color = colors.shift();
      colors.push(color);
      return '<div id="color-demo" hx-get="/colors" hx-swap="outerHTML" class="smooth" hx-trigger="every 1s" style="color:' + color + '">\n'+
             '  Color Swap Demo\n'+
             '</div>\n'
    });
</script>### <a class="zola-anchor" href="#smooth-progress-bar" aria-label="Anchor link for: smooth-progress-bar">#</a>Smooth Progress BarThe <a href="https://htmx.org/examples/progress-bar/">Progress Bar</a> demo uses this basic CSS animation technique as well, by updating the <code>length</code>
property of a progress bar element, allowing for a smooth animation.

<h2 id="swapping"><a class="zola-anchor" href="#swapping" aria-label="Anchor link for: swapping">#</a>Swap Transitions</h2>### <a class="zola-anchor" href="#fade-out-on-swap" aria-label="Anchor link for: fade-out-on-swap">#</a>Fade Out On SwapIf you want to fade out an element that is going to be removed when the request ends, you want to take advantage
of the <code>htmx-swapping</code> class with some CSS and extend the swap phase to be long enough for your animation to
complete.  This can be done like so:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span style="color:#d19a66;">.fade-me-out.htmx-swapping </span><span>{
</span><span>  opacity: </span><span style="color:#d19a66;">0</span><span>;
</span><span>  transition: opacity </span><span style="color:#d19a66;">1s </span><span>ease-out;
</span><span>}
</span><span>&lt;/</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"fade-me-out"
</span><span>        </span><span style="color:#d19a66;">hx-delete</span><span>=</span><span style="color:#98c379;">"/fade_out_demo"
</span><span>        </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML swap:1s"</span><span>&gt;
</span><span>        Fade Me Out
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre><h4 id="fade-swap-demo"><a class="zola-anchor" href="#fade-swap-demo" aria-label="Anchor link for: fade-swap-demo">#</a>Demo</h4><style>
.fade-me-out.htmx-swapping {
  opacity: 0;
  transition: opacity 1s ease-out;
}
</style><button class="fade-me-out" hx-delete="/fade_out_demo" hx-swap="outerHTML swap:1s">
Delete Me
</button>

<script>
    onDelete("/fade_out_demo", function () {return ""});
</script><h2 id="settling"><a class="zola-anchor" href="#settling" aria-label="Anchor link for: settling">#</a>Settling Transitions</h2>### <a class="zola-anchor" href="#fade-in-on-addition" aria-label="Anchor link for: fade-in-on-addition">#</a>Fade In On AdditionBuilding on the last example, we can fade in the new content by using the <code>htmx-added</code> class during the settle
phase.  You can also write CSS transitions against the target, rather than the new content, by using the <code>htmx-settling</code>
class.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span style="color:#d19a66;">#fade-me-in.htmx-added </span><span>{
</span><span>  opacity: </span><span style="color:#d19a66;">0</span><span>;
</span><span>}
</span><span style="color:#d19a66;">#fade-me-in </span><span>{
</span><span>  opacity: </span><span style="color:#d19a66;">1</span><span>;
</span><span>  transition: opacity </span><span style="color:#d19a66;">1s </span><span>ease-out;
</span><span>}
</span><span>&lt;/</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"fade-me-in"
</span><span>        </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary"
</span><span>        </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/fade_in_demo"
</span><span>        </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML settle:1s"</span><span>&gt;
</span><span>        Fade Me In
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre><h4 id="fade-settle-demo"><a class="zola-anchor" href="#fade-settle-demo" aria-label="Anchor link for: fade-settle-demo">#</a>Demo</h4><style>
#fade-me-in.htmx-added {
  opacity: 0;
}
#fade-me-in {
  opacity: 1;
  transition: opacity 1s ease-out;
}
</style><button id="fade-me-in" class="btn primary" hx-post="/fade_me_in" hx-swap="outerHTML settle:1s">
Fade Me In
</button>

<script>
    onPost("/fade_me_in", function () {return "<button id=\"fade-me-in\"\n"+
                                               "        class=\"btn primary\"\n"+
                                               "        hx-post=\"/fade_me_in\"\n"+
                                               "        hx-swap=\"outerHTML settle:1s\">\n"+
                                               "        Fade Me In\n"+
                                               "</button>"});
</script><h2 id="request"><a class="zola-anchor" href="#request" aria-label="Anchor link for: request">#</a>Request In Flight Animation</h2>You can also take advantage of the <code>htmx-request</code> class, which is applied to the element that triggers a request.  Below
is a form that on submit will change its look to indicate that a request is being processed:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span>  </span><span style="color:#e06c75;">form</span><span style="color:#d19a66;">.htmx-request </span><span>{
</span><span>    opacity: </span><span style="color:#d19a66;">.5</span><span>;
</span><span>    transition: opacity </span><span style="color:#d19a66;">300ms </span><span>linear;
</span><span>  }
</span><span>&lt;/</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/name" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML"</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">label</span><span>&gt;Name:&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"name"</span><span>&gt;&lt;</span><span style="color:#e06c75;">br</span><span>/&gt;
</span><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary"</span><span>&gt;Submit&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre><h4 id="request-demo"><a class="zola-anchor" href="#request-demo" aria-label="Anchor link for: request-demo">#</a>Demo</h4><style>
  form.htmx-request {
    opacity: .5;
    transition: opacity 300ms linear;
  }
</style><div aria-live="polite">
<form hx-post="/name" hx-swap="outerHTML">
<label>Name:</label><input name="name"><br>
<button class="btn primary">Submit</button>
</form>
</div><script>
  onPost("/name", function(){ return "Submitted!"; });
</script><h2 id="using-the-htmx-class-tools-extension"><a class="zola-anchor" href="#using-the-htmx-class-tools-extension" aria-label="Anchor link for: using-the-htmx-class-tools-extension">#</a>Using the htmx <code>class-tools</code> Extension</h2>Many interesting animations can be created by using the <a rel="noopener" target="_blank" href="https://github.com/bigskysoftware/htmx-extensions/blob/main/src/class-tools/README.md"><code>class-tools</code></a> extension.

Here is an example that toggles the opacity of a div.  Note that we set the toggle time to be a bit longer than
the transition time.  This avoids flickering that can happen if the transition is interrupted by a class change.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span style="color:#d19a66;">.demo.faded </span><span>{
</span><span>  opacity:</span><span style="color:#d19a66;">.3</span><span>;
</span><span>}
</span><span style="color:#d19a66;">.demo </span><span>{
</span><span>  opacity:</span><span style="color:#d19a66;">1</span><span>;
</span><span>  transition: opacity ease-in </span><span style="color:#d19a66;">900ms</span><span>;
</span><span>}
</span><span>&lt;/</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"demo" </span><span style="color:#d19a66;">classes</span><span>=</span><span style="color:#98c379;">"toggle faded:1s"</span><span>&gt;Toggle Demo&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h4 id="class-tools-demo"><a class="zola-anchor" href="#class-tools-demo" aria-label="Anchor link for: class-tools-demo">#</a>Demo</h4><style>
.demo.faded {
  opacity:.3;
}
.demo {
  opacity:1;
  transition: opacity ease-in 900ms;
}
</style><div class="demo" classes="toggle faded:1s">Toggle Demo</div>### <a class="zola-anchor" href="#view-transitions" aria-label="Anchor link for: view-transitions">#</a>Using the View Transition APIhtmx provides access to the new  <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API">View Transitions API</a>
via the <code>transition</code> option of the <a href="/attributes/hx-swap"><code>hx-swap</code></a> attribute.

Below is an example of a swap that uses a view transition.  The transition is tied to the outer div via a
<code>view-transition-name</code> property in CSS, and that transition is defined in terms of <code>::view-transition-old</code>
and <code>::view-transition-new</code>, using <code>@keyframes</code> to define the animation.  (Fuller details on the View Transition
API can be found on the <a rel="noopener" target="_blank" href="https://developer.chrome.com/docs/web-platform/view-transitions/">Chrome Developer Page</a> on them.)

The old content of this transition should slide out to the left and the new content should slide in from the right.

Note that, as of this writing, the visual transition will only occur on Chrome 111+, but more browsers are expected to
implement this feature in the near future.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span>   </span><span style="color:#c678dd;">@keyframes </span><span>fade-in {
</span><span>     </span><span style="color:#c678dd;">from </span><span>{ opacity: </span><span style="color:#d19a66;">0</span><span>; }
</span><span>   }
</span><span>
</span><span>   </span><span style="color:#c678dd;">@keyframes </span><span>fade-out {
</span><span>     </span><span style="color:#c678dd;">to </span><span>{ opacity: </span><span style="color:#d19a66;">0</span><span>; }
</span><span>   }
</span><span>
</span><span>   </span><span style="color:#c678dd;">@keyframes </span><span>slide-from-right {
</span><span>     </span><span style="color:#c678dd;">from </span><span>{ transform: </span><span style="color:#56b6c2;">translateX</span><span>(</span><span style="color:#d19a66;">90px</span><span>); }
</span><span>   }
</span><span>
</span><span>   </span><span style="color:#c678dd;">@keyframes </span><span>slide-to-left {
</span><span>     </span><span style="color:#c678dd;">to </span><span>{ transform: </span><span style="color:#56b6c2;">translateX</span><span>(</span><span style="color:#d19a66;">-90px</span><span>); }
</span><span>   }
</span><span>
</span><span>   </span><span style="color:#d19a66;">.slide-it </span><span>{
</span><span>     view-transition-name: slide-it;
</span><span>   }
</span><span>
</span><span>   </span><span style="color:#d19a66;">::</span><span style="color:#c678dd;">view-transition-old(</span><span style="color:#e06c75;">slide-it</span><span>) {
</span><span>     animation: </span><span style="color:#d19a66;">180ms </span><span style="color:#56b6c2;">cubic-bezier</span><span>(</span><span style="color:#d19a66;">0.4</span><span>, </span><span style="color:#d19a66;">0</span><span>, </span><span style="color:#d19a66;">1</span><span>, </span><span style="color:#d19a66;">1</span><span>) both fade-out,
</span><span>     </span><span style="color:#d19a66;">600ms </span><span style="color:#56b6c2;">cubic-bezier</span><span>(</span><span style="color:#d19a66;">0.4</span><span>, </span><span style="color:#d19a66;">0</span><span>, </span><span style="color:#d19a66;">0.2</span><span>, </span><span style="color:#d19a66;">1</span><span>) both slide-to-left;
</span><span>   }
</span><span>   </span><span style="color:#d19a66;">::</span><span style="color:#c678dd;">view-transition-new(</span><span style="color:#e06c75;">slide-it</span><span>) {
</span><span>     animation: </span><span style="color:#d19a66;">420ms </span><span style="color:#56b6c2;">cubic-bezier</span><span>(</span><span style="color:#d19a66;">0</span><span>, </span><span style="color:#d19a66;">0</span><span>, </span><span style="color:#d19a66;">0.2</span><span>, </span><span style="color:#d19a66;">1</span><span>) </span><span style="color:#d19a66;">90ms </span><span>both fade-in,
</span><span>     </span><span style="color:#d19a66;">600ms </span><span style="color:#56b6c2;">cubic-bezier</span><span>(</span><span style="color:#d19a66;">0.4</span><span>, </span><span style="color:#d19a66;">0</span><span>, </span><span style="color:#d19a66;">0.2</span><span>, </span><span style="color:#d19a66;">1</span><span>) both slide-from-right;
</span><span>   }
</span><span>&lt;/</span><span style="color:#e06c75;">style</span><span>&gt;
</span><span>
</span><span>
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"slide-it"</span><span>&gt;
</span><span>   &lt;</span><span style="color:#e06c75;">h1</span><span>&gt;Initial Content&lt;/</span><span style="color:#e06c75;">h1</span><span>&gt;
</span><span>   &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/new-content" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"innerHTML transition:true" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"closest div"</span><span>&gt;
</span><span>     Swap It!
</span><span>   &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h4 id="demo"><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">#</a>Demo</h4><style>
   @keyframes fade-in {
     from { opacity: 0; }
   }

   @keyframes fade-out {
     to { opacity: 0; }
   }

   @keyframes slide-from-right {
     from { transform: translateX(90px); }
   }

   @keyframes slide-to-left {
     to { transform: translateX(-90px); }
   }

   .slide-it {
     view-transition-name: slide-it;
   }

   ::view-transition-old(slide-it) {
     animation: 180ms cubic-bezier(0.4, 0, 1, 1) both fade-out,
     600ms cubic-bezier(0.4, 0, 0.2, 1) both slide-to-left;
   }
   ::view-transition-new(slide-it) {
     animation: 420ms cubic-bezier(0, 0, 0.2, 1) 90ms both fade-in,
     600ms cubic-bezier(0.4, 0, 0.2, 1) both slide-from-right;
   }
</style><div class="slide-it">
   <h1>Initial Content</h1>
   <button class="btn primary" hx-get="/new-content" hx-swap="innerHTML transition:true" hx-target="closest div">
     Swap It!
   </button>
</div><script>
    var originalContent = htmx.find(".slide-it").innerHTML;

    this.server.respondWith("GET", "/new-content", function(xhr){
        xhr.respond(200,  {}, "<h1>New Content</h1> <button class='btn danger' hx-get='/original-content' hx-swap='innerHTML transition:true' hx-target='closest div'>Restore It! </button>")
    });

    this.server.respondWith("GET", "/original-content", function(xhr){
        xhr.respond(200,  {}, originalContent)
    });
</script><h2 id="conclusion"><a class="zola-anchor" href="#conclusion" aria-label="Anchor link for: conclusion">#</a>Conclusion</h2>You can use the techniques above to create quite a few interesting and pleasing effects with plain old HTML while using htmx.

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Value Select

URL: https://htmx.org/examples/value-select/

<h1>Cascading Selects</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>In this example we show how to make the values in one <code>select</code> depend on the value selected in another <code>select</code>.

To begin we start with a default value for the <code>make</code> select: Audi.  We render the <code>model</code> select for this make.  We
then have the <code>make</code> select trigger a <code>GET</code> to <code>/models</code> to retrieve the models options and target the <code>models</code> select.

Here is the code:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">label </span><span>&gt;Make&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">select </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"make" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/models" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#models" </span><span style="color:#d19a66;">hx-indicator</span><span>=</span><span style="color:#98c379;">".htmx-indicator"</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">option </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">"audi"</span><span>&gt;Audi&lt;/</span><span style="color:#e06c75;">option</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">option </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">"toyota"</span><span>&gt;Toyota&lt;/</span><span style="color:#e06c75;">option</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">option </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">"bmw"</span><span>&gt;BMW&lt;/</span><span style="color:#e06c75;">option</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">select</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">label</span><span>&gt;Model&lt;/</span><span style="color:#e06c75;">label</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">select </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"models" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"model"</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">option </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">"a1"</span><span>&gt;A1&lt;/</span><span style="color:#e06c75;">option</span><span>&gt;
</span><span>      ...
</span><span>    &lt;/</span><span style="color:#e06c75;">select</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">img </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"htmx-indicator" </span><span style="color:#d19a66;">width</span><span>=</span><span style="color:#98c379;">"20" </span><span style="color:#d19a66;">src</span><span>=</span><span style="color:#98c379;">"/img/bars.svg"</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>When a request is made to the <code>/models</code> end point, we return the models for that make:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">option </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'325i'</span><span>&gt;325i&lt;/</span><span style="color:#e06c75;">option</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">option </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'325ix'</span><span>&gt;325ix&lt;/</span><span style="color:#e06c75;">option</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">option </span><span style="color:#d19a66;">value</span><span>=</span><span style="color:#98c379;">'X5'</span><span>&gt;X5&lt;/</span><span style="color:#e06c75;">option</span><span>&gt; 
</span></code></pre>And they become available in the <code>model</code> select.

<style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><script>

    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // routes
    init("/demo", function(request, params){
      return formTemplate();
    });
    
    onGet(/models.*/, function (request, params) {
        var make = dataStore.findMake(params['make']);
        return modelOptionsTemplate(make['models']);
    });
    
    // templates
    function formTemplate() {
      return `  ### Pick A Make/Model              
<form>
  <div>
    <label >Make</label>
    <select name="make" hx-get="/models" hx-target="#models" hx-indicator=".htmx-indicator">
      <option value="audi">Audi</option>
      <option value="toyota">Toyota</option>
      <option value="bmw">BMW</option>
    </select>
  </div>
  <div>
    <label>Model</label>
    <select id="models" name="model">
      <option value="a1">A1</option>
      <option value="a3">A3</option>
      <option value="a6">A6</option>
    </select>
    <img class="htmx-indicator" width="20" src="/img/bars.svg">    
  </div>
</form>`;
    }

    function modelOptionsTemplate(make) {
      return make.map(function(val) {
        return "<option value='" + val + "'>" + val +"</option>";
      }).join("\n");
    }

    var dataStore = function(){
      var data = {
        audi : { models : ["A1", "A4", "A6"] },
        toyota : { models : ["Landcruiser", "Tacoma", "Yaris"] },
        bmw : { models : ["325i", "325ix", "X5"] }
      };
      return {
        findMake : function(make) {
          return data[make];
        }
      }
    }()
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Progress Bar

URL: https://htmx.org/examples/progress-bar/

<h1>Progress Bar</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>This example shows how to implement a smoothly scrolling progress bar.

We start with an initial state with a button that issues a <code>POST</code> to <code>/start</code> to begin the job:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"this" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">h3</span><span>&gt;Start Progress&lt;/</span><span style="color:#e06c75;">h3</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary" </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/start"</span><span>&gt;
</span><span>            Start Job
</span><span>  &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This div is then replaced with a new div containing status and a progress bar that reloads itself every 600ms:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"done" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/job" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"this"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">h3 </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"status" </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"pblabel" </span><span style="color:#d19a66;">tabindex</span><span>=</span><span style="color:#98c379;">"-1" </span><span style="color:#d19a66;">autofocus</span><span>&gt;Running&lt;/</span><span style="color:#e06c75;">h3</span><span>&gt;
</span><span>
</span><span>  &lt;</span><span style="color:#e06c75;">div
</span><span>    </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/job/progress"
</span><span>    </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"every 600ms"
</span><span>    </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"this"
</span><span>    </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"innerHTML"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"progress" </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"progressbar" </span><span style="color:#d19a66;">aria-valuemin</span><span>=</span><span style="color:#98c379;">"0" </span><span style="color:#d19a66;">aria-valuemax</span><span>=</span><span style="color:#98c379;">"100" </span><span style="color:#d19a66;">aria-valuenow</span><span>=</span><span style="color:#98c379;">"0" </span><span style="color:#d19a66;">aria-labelledby</span><span>=</span><span style="color:#98c379;">"pblabel"</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"pb" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"progress-bar" </span><span style="color:#d19a66;">style</span><span>=</span><span style="color:#98c379;">"</span><span>width:</span><span style="color:#d19a66;">0%</span><span style="color:#98c379;">"</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>
</span></code></pre>This progress bar is updated every 600 milliseconds, with the “width” style attribute and <code>aria-valuenow</code> attributed set to current progress value.
Because there is an id on the progress bar div, htmx will smoothly transition between requests by settling the
style attribute into its new value.  This, when coupled with CSS transitions, makes the visual transition continuous
rather than jumpy.

Finally, when the process is complete, a server returns <code>HX-Trigger: done</code> header, which triggers an update of the UI to “Complete” state
with a restart button added to the UI (we are using the <a rel="noopener" target="_blank" href="https://github.com/bigskysoftware/htmx-extensions/blob/main/src/class-tools/README.md"><code>class-tools</code></a> extension in this example to add fade-in effect on the button):

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"done" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/job" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"this"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">h3 </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"status" </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"pblabel" </span><span style="color:#d19a66;">tabindex</span><span>=</span><span style="color:#98c379;">"-1" </span><span style="color:#d19a66;">autofocus</span><span>&gt;Complete&lt;/</span><span style="color:#e06c75;">h3</span><span>&gt;
</span><span>
</span><span>  &lt;</span><span style="color:#e06c75;">div
</span><span>    </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/job/progress"
</span><span>    </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"none"
</span><span>    </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"this"
</span><span>    </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"innerHTML"</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"progress" </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"progressbar" </span><span style="color:#d19a66;">aria-valuemin</span><span>=</span><span style="color:#98c379;">"0" </span><span style="color:#d19a66;">aria-valuemax</span><span>=</span><span style="color:#98c379;">"100" </span><span style="color:#d19a66;">aria-valuenow</span><span>=</span><span style="color:#98c379;">"122" </span><span style="color:#d19a66;">aria-labelledby</span><span>=</span><span style="color:#98c379;">"pblabel"</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"pb" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"progress-bar" </span><span style="color:#d19a66;">style</span><span>=</span><span style="color:#98c379;">"</span><span>width:</span><span style="color:#d19a66;">122%</span><span style="color:#98c379;">"</span><span>&gt;
</span><span>      &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>
</span><span>  &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"restart-btn" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary" </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/start" </span><span style="color:#d19a66;">classes</span><span>=</span><span style="color:#98c379;">"add show:600ms"</span><span>&gt;
</span><span>    Restart Job
</span><span>  &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This example uses styling cribbed from the bootstrap progress bar:

<pre data-lang="css" style="background-color:#1f2329;color:#abb2bf;" class="language-css "><code class="language-css" data-lang="css"><span style="color:#d19a66;">.progress </span><span>{
</span><span>    height: </span><span style="color:#d19a66;">20px</span><span>;
</span><span>    margin-bottom: </span><span style="color:#d19a66;">20px</span><span>;
</span><span>    overflow: hidden;
</span><span>    background-color: </span><span style="color:#56b6c2;">#f5f5f5</span><span>;
</span><span>    border-radius: </span><span style="color:#d19a66;">4px</span><span>;
</span><span>    box-shadow: inset </span><span style="color:#d19a66;">0 1px 2px </span><span style="color:#56b6c2;">rgba</span><span>(</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">.1</span><span>);
</span><span>}
</span><span style="color:#d19a66;">.progress-bar </span><span>{
</span><span>    float: left;
</span><span>    width: </span><span style="color:#d19a66;">0%</span><span>;
</span><span>    height: </span><span style="color:#d19a66;">100%</span><span>;
</span><span>    font-size: </span><span style="color:#d19a66;">12px</span><span>;
</span><span>    line-height: </span><span style="color:#d19a66;">20px</span><span>;
</span><span>    color: </span><span style="color:#56b6c2;">#fff</span><span>;
</span><span>    text-align: center;
</span><span>    background-color: </span><span style="color:#56b6c2;">#337ab7</span><span>;
</span><span>    -webkit-box-shadow: inset </span><span style="color:#d19a66;">0 -1px 0 </span><span style="color:#56b6c2;">rgba</span><span>(</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">.15</span><span>);
</span><span>    box-shadow: inset </span><span style="color:#d19a66;">0 -1px 0 </span><span style="color:#56b6c2;">rgba</span><span>(</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">0</span><span>,</span><span style="color:#d19a66;">.15</span><span>);
</span><span>    -webkit-transition: width </span><span style="color:#d19a66;">.6s </span><span>ease;
</span><span>    -o-transition: width </span><span style="color:#d19a66;">.6s </span><span>ease;
</span><span>    transition: width </span><span style="color:#d19a66;">.6s </span><span>ease;
</span><span>}
</span></code></pre><style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><style>
.progress {
    height: 20px;
    margin-bottom: 20px;
    overflow: hidden;
    background-color: #f5f5f5;
    border-radius: 4px;
    box-shadow: inset 0 1px 2px rgba(0,0,0,.1);
}
.progress-bar {
    float: left;
    width: 0%;
    height: 100%;
    font-size: 12px;
    line-height: 20px;
    color: #fff;
    text-align: center;
    background-color: #337ab7;
    -webkit-box-shadow: inset 0 -1px 0 rgba(0,0,0,.15);
    box-shadow: inset 0 -1px 0 rgba(0,0,0,.15);
    -webkit-transition: width .6s ease;
    -o-transition: width .6s ease;
    transition: width .6s ease;
}
#restart-btn {
  opacity:0;
}
#restart-btn.show {
  opacity:1;
  transition: opacity 100ms ease-in;
}
</style><script>

    //=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // routes
    init("/demo", function(request, params){
      return startButton("Start Progress");
    });

    onPost("/start", function(request, params){
        var job = jobManager.start();
        return jobStatusTemplate(job);
    });

    onGet("/job", function(request, params){
        var job = jobManager.currentProcess();
        return jobStatusTemplate(job);
    });

    onGet("/job/progress", function(request, params, responseHeaders){
        var job = jobManager.currentProcess();

        if (job.complete) {
          responseHeaders["HX-Trigger"] = "done";
        }
        return jobProgressTemplate(job);
    });

    // templates
    function startButton(message) {
      return `<div hx-target="this" hx-swap="outerHTML">
  ### ${message}
  <button class="btn primary" hx-post="/start">
            Start Job
  </button>
</div>`;
    }

    function jobProgressTemplate(job) {
      return `<div class="progress" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${job.percentComplete}" aria-labelledby="pblabel">
      <div id="pb" class="progress-bar" style="width:${job.percentComplete}%">
    </div>
  </div>`
    }

    function jobStatusTemplate(job) {
        return `<div hx-trigger="done" hx-get="/job" hx-swap="outerHTML" hx-target="this">
  ### ${job.complete ? "Complete" : "Running"}

  <div
    hx-get="/job/progress"
    hx-trigger="${job.complete ? 'none' : 'every 600ms'}"
    hx-target="this"
    hx-swap="innerHTML">
    ${jobProgressTemplate(job)}
  </div>
  ${restartButton(job)}`;
    }

    function restartButton(job) {
      if(job.complete){
        return `
<button id="restart-btn" class="btn primary" hx-post="/start" classes="add show:600ms">
  Restart Job
</button>`
      } else {
        return "";
      }
    }

    var jobManager = (function(){
      var currentProcess = null;
      return {
        start : function() {
          currentProcess = {
            complete : false,
            percentComplete : 0
          }
          return currentProcess;
        },
        currentProcess : function() {
          currentProcess.percentComplete += Math.min(100, Math.floor(33 * Math.random()));  // simulate progress
          currentProcess.complete = currentProcess.percentComplete >= 100;
          return currentProcess;
        }
      }
    })();
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# Dialogs - Bootstrap

URL: https://htmx.org/examples/modal-bootstrap/

<h1>Modal Dialogs in Bootstrap</h1><script src="https://unpkg.com/sinon@9.0.2/pkg/sinon.js"></script><script src="/js/demo.js"></script>Many CSS toolkits include styles (and Javascript) for creating modal dialog boxes.
This example shows how to use HTMX alongside original JavaScript provided by Bootstrap.

We start with a button that triggers the dialog, along with a DIV at the bottom of your
markup where the dialog will be loaded:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button
</span><span>    </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/modal"
</span><span>    </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#modals-here"
</span><span>    </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"click"
</span><span>    </span><span style="color:#d19a66;">data-bs-toggle</span><span>=</span><span style="color:#98c379;">"modal"
</span><span>    </span><span style="color:#d19a66;">data-bs-target</span><span>=</span><span style="color:#98c379;">"#modals-here"
</span><span>    </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn primary"</span><span>&gt;Open Modal&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"modals-here"
</span><span>    </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"modal modal-blur fade"
</span><span>    </span><span style="color:#d19a66;">style</span><span>=</span><span style="color:#98c379;">"</span><span>display: none</span><span style="color:#98c379;">"
</span><span>    </span><span style="color:#d19a66;">aria-hidden</span><span>=</span><span style="color:#98c379;">"false"
</span><span>    </span><span style="color:#d19a66;">tabindex</span><span>=</span><span style="color:#98c379;">"-1"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"modal-dialog modal-lg modal-dialog-centered" </span><span style="color:#d19a66;">role</span><span>=</span><span style="color:#98c379;">"document"</span><span>&gt;
</span><span>        &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"modal-content"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This button uses a <code>GET</code> request to <code>/modal</code> when this button is clicked.  The
contents of this file will be added to the DOM underneath the <code>#modals-here</code> DIV.

The server responds with a slightly modified version of Bootstrap’s standard modal

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"modal-dialog modal-dialog-centered"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"modal-content"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"modal-header"</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">h5 </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"modal-title"</span><span>&gt;Modal title&lt;/</span><span style="color:#e06c75;">h5</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"modal-body"</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">p</span><span>&gt;Modal body text goes here.&lt;/</span><span style="color:#e06c75;">p</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"modal-footer"</span><span>&gt;
</span><span>      &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"button" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"btn btn-secondary" </span><span style="color:#d19a66;">data-bs-dismiss</span><span>=</span><span style="color:#98c379;">"modal"</span><span>&gt;Close&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>    &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><div id="modals-here" class="modal modal-blur fade" style="display: none" aria-hidden="false" tabindex="-1">
    <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
        <div class="modal-content"></div>
    </div>
</div><style>
  #demo-server-info {
      padding: 8px;
      position: fixed;
      bottom: 0;
      right: 0;
      left: 0;
      height: 64px;
      width: 100vw;
      background-color: whitesmoke;
      border-top: 2px solid gray;
      overflow: hide;
      margin: 0px;
      z-index: 1;
  }
  #demo-server-info.show {
      max-height: 45vh;
      height: 500px;
      overflow: scroll;
  }
  #demo-activity {
      height:300px
  }

  #demo-activity div {
      vertical-align: top
  }

  #demo-activity ol li {
      list-style-position: inside;
  }

  #demo-canvas {
      margin-bottom: 500px;
      padding-top: 12px;
  }

  @media (prefers-color-scheme: dark) {
    #demo-server-info {
      background-color: var(--footerBackground);
    }
  }
</style><script>
  function toggleRequestInfo() {
      var classList = document.getElementById("demo-server-info").classList;
      classList.toggle("show");
      if (classList.contains('show')) {
          document.getElementById("request-info-toggler").innerHTML = "&downarrow; Hide"
      } else {
          document.getElementById("request-info-toggler").innerHTML = "&uparrow; Show"
      }
  }
</script><div id="demo-server-info">
  <div>Server Requests<span id="request-count"></span> <a id="request-info-toggler" onclick="toggleRequestInfo()" style="cursor: pointer">&amp;uparrow; Show</a></div>
  <div id="demo-activity" class="row">
      <div class="3 col">
          <ol id="demo-timeline" reversed>
          </ol>
      </div>
      <div id="demo-current-request" class="9 col">
      </div>
  </div>
</div><h2><a class="zola-anchor" href="#demo" aria-label="Anchor link for: demo">🔗</a>Demo</h2><div id="demo-canvas">
</div><style>
	@import "https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.2.2/css/bootstrap.min.css";
</style><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script><script>

	//=========================================================================
    // Fake Server Side Code
    //=========================================================================

    // routes
    init("/demo", function(request, params) {
		return `<button
	hx-get="/modal"
	hx-target="#modals-here"
	hx-trigger="click"
    data-bs-toggle="modal"
    data-bs-target="#modals-here"
	class="btn primary">Open Modal</button>
	`})

	onGet("/modal", function(request, params){
	  return `<div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title">Modal title</h5>
        </div>
        <div class="modal-body">
            Modal body text goes here.


        </div>
    <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
    </div>
    </div>
</div>`
});
</script><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

