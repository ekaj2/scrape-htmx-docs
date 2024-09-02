# hx-select-oob

URL: https://htmx.org/attributes/hx-select-oob/

<h1><code>hx-select-oob</code></h1>The <code>hx-select-oob</code> attribute allows you to select content from a response to be swapped in via an out-of-band swap.<br>
The value of this attribute is comma separated list of elements to be swapped out of band.  This attribute is almost
always paired with <a href="https://htmx.org/attributes/hx-select/">hx-select</a>.

Here is an example that selects a subset of the response content:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>   &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"alert"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/info" 
</span><span>            </span><span style="color:#d19a66;">hx-select</span><span>=</span><span style="color:#98c379;">"#info-details" 
</span><span>            </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML"
</span><span>            </span><span style="color:#d19a66;">hx-select-oob</span><span>=</span><span style="color:#98c379;">"#alert"</span><span>&gt;
</span><span>        Get Info!
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This button will issue a <code>GET</code> to <code>/info</code> and then select the element with the id <code>info-details</code>,
which will replace the entire button in the DOM, and, in addition, pick out an element with the id <code>alert</code>
in the response and swap it in for div in the DOM with the same ID.

Each value in the comma separated list of values can specify any valid <a href="https://htmx.org/attributes/hx-swap/"><code>hx-swap</code></a>
strategy by separating the selector and the swap strategy with a <code>:</code>.

For example, to prepend the alert content instead of replacing it:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>   &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"alert"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/info"
</span><span>            </span><span style="color:#d19a66;">hx-select</span><span>=</span><span style="color:#98c379;">"#info-details"
</span><span>            </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML"
</span><span>            </span><span style="color:#d19a66;">hx-select-oob</span><span>=</span><span style="color:#98c379;">"#alert:afterbegin"</span><span>&gt;
</span><span>        Get Info!
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h2 id="notes">Notes</h2>- <code>hx-select-oob</code> is inherited and can be placed on a parent element

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# HX-Push-Url

URL: https://htmx.org/headers/hx-push-url/

<h1>HX-Push-Url Response Header</h1>The <code>HX-Push-Url</code> header allows you to push a URL into the browser <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">location history</a>.
This creates a new history entry, allowing navigation with the browser’s back and forward buttons.
This is similar to the <a href="https://htmx.org/attributes/hx-push-url/"><code>hx-push-url</code> attribute</a>.

If present, this header overrides any behavior defined with attributes.

The possible values for this header are:

<ol>
<li>A URL to be pushed into the location bar.
This may be relative or absolute, as per <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/History/pushState"><code>history.pushState()</code></a>.</li>
<li><code>false</code>, which prevents the browser’s history from being updated.</li>
</ol><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-push-url

URL: https://htmx.org/attributes/hx-push-url/

<h1><code>hx-push-url</code></h1>The <code>hx-push-url</code> attribute allows you to push a URL into the browser <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">location history</a>.
This creates a new history entry, allowing navigation with the browser’s back and forward buttons.
htmx snapshots the current DOM and saves it into its history cache, and restores from this cache on navigation.

The possible values of this attribute are:

<ol>
<li><code>true</code>, which pushes the fetched URL into history.</li>
<li><code>false</code>, which disables pushing the fetched URL if it would otherwise be pushed due to inheritance or <a href="/attributes/hx-boost"><code>hx-boost</code></a>.</li>
<li>A URL to be pushed into the location bar.
This may be relative or absolute, as per <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/History/pushState"><code>history.pushState()</code></a>.</li>
</ol>Here is an example:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/account" </span><span style="color:#d19a66;">hx-push-url</span><span>=</span><span style="color:#98c379;">"true"</span><span>&gt;
</span><span>  Go to My Account
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This will cause htmx to snapshot the current DOM to <code>localStorage</code> and push the URL `/account’ into the browser location bar.

Another example:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/account" </span><span style="color:#d19a66;">hx-push-url</span><span>=</span><span style="color:#98c379;">"/account/home"</span><span>&gt;
</span><span>  Go to My Account
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This will push the URL `/account/home’ into the location history.

<h2 id="notes">Notes</h2>- <code>hx-push-url</code> is inherited and can be placed on a parent element
- The <a href="https://htmx.org/headers/hx-push-url/"><code>HX-Push-Url</code> response header</a> has similar behavior and can override this attribute.
- The <a href="https://htmx.org/attributes/hx-history-elt/"><code>hx-history-elt</code> attribute</a> allows changing which element is saved in the history cache.

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-select

URL: https://htmx.org/attributes/hx-select/

<h1><code>hx-select</code></h1>The <code>hx-select</code> attribute allows you to select the content you want swapped from a response.  The value of
this attribute is a CSS query selector of the element or elements to select from the response.

Here is an example that selects a subset of the response content:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/info" </span><span style="color:#d19a66;">hx-select</span><span>=</span><span style="color:#98c379;">"#info-details" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML"</span><span>&gt;
</span><span>        Get Info!
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>So this button will issue a <code>GET</code> to <code>/info</code> and then select the element with the id <code>info-detail</code>,
which will replace the entire button in the DOM.

<h2 id="notes">Notes</h2>- <code>hx-select</code> is inherited and can be placed on a parent element

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-get

URL: https://htmx.org/attributes/hx-get/

<h1><code>hx-get</code></h1>The <code>hx-get</code> attribute will cause an element to issue a <code>GET</code> to the specified URL and swap
the HTML into the DOM using a swap strategy:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example"</span><span>&gt;Get Some HTML&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This example will cause the <code>div</code> to issue a <code>GET</code> to <code>/example</code> and swap the returned HTML into
the <code>innerHTML</code> of the <code>div</code>.

### Notes- <code>hx-get</code> is not inherited
- By default <code>hx-get</code> does not include any parameters.  You can use the <a href="https://htmx.org/attributes/hx-params/">hx-params</a>
attribute to change this
- You can control the target of the swap using the <a href="https://htmx.org/attributes/hx-target/">hx-target</a> attribute
- You can control the swap strategy by using the <a href="https://htmx.org/attributes/hx-swap/">hx-swap</a> attribute
- You can control what event triggers the request with the <a href="https://htmx.org/attributes/hx-trigger/">hx-trigger</a> attribute
- You can control the data submitted with the request in various ways, documented here: <a href="https://htmx.org/docs/#parameters">Parameters</a>
- An empty <code>hx-get:""</code> will make a get request to the current url and will swap the current HTML page

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-post

URL: https://htmx.org/attributes/hx-post/

<h1><code>hx-post</code></h1>The <code>hx-post</code> attribute will cause an element to issue a <code>POST</code> to the specified URL and swap
the HTML into the DOM using a swap strategy:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/account/enable" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"body"</span><span>&gt;
</span><span>  Enable Your Account
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>This example will cause the <code>button</code> to issue a <code>POST</code> to <code>/account/enable</code> and swap the returned HTML into
the <code>innerHTML</code> of the <code>body</code>.

<h2 id="notes">Notes</h2>- <code>hx-post</code> is not inherited
- You can control the target of the swap using the <a href="https://htmx.org/attributes/hx-target/">hx-target</a> attribute
- You can control the swap strategy by using the <a href="https://htmx.org/attributes/hx-swap/">hx-swap</a> attribute
- You can control what event triggers the request with the <a href="https://htmx.org/attributes/hx-trigger/">hx-trigger</a> attribute
- You can control the data submitted with the request in various ways, documented here: <a href="https://htmx.org/docs/#parameters">Parameters</a>

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-on*

URL: https://htmx.org/attributes/hx-on/

<h1><code>hx-on</code></h1>The <code>hx-on*</code> attributes allow you to embed scripts inline to respond to events directly on an element; similar to the
<a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/Events/Event_handlers#using_onevent_properties"><code>onevent</code> properties</a> found in HTML, such as <code>onClick</code>.

The <code>hx-on*</code> attributes improve upon <code>onevent</code> by enabling the handling of any arbitrary JavaScript event,
for enhanced <a href="/essays/locality-of-behaviour/">Locality of Behaviour (LoB)</a> even when dealing with non-standard DOM events. For example, these
attributes allow you to handle <a href="/reference#events">htmx events</a>.

With <code>hx-on</code> attributes, you specify the event name as part of the attribute name, after a colon.  So, for example, if
you want to respond to a <code>click</code> event, you would use the attribute <code>hx-on:click</code>:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-on:click</span><span>=</span><span style="color:#98c379;">"alert('Clicked!')"</span><span>&gt;Click&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>Note that this syntax can be used to capture all htmx events, as well as most other custom events, in addition to the
standard DOM events.

One gotcha to note is that DOM attributes do not preserve case. This means, unfortunately, an attribute like
<code>hx-on:htmx:beforeRequest</code> <strong>will not work</strong>, because the DOM lowercases the attribute names.  Fortunately, htmx supports
both camel case event names and also <a href="https://htmx.org/docs/#events">kebab-case event names</a>, so you can use <code>hx-on:htmx:before-request</code> instead.

In order to make writing htmx-based event handlers a little easier, you can use the shorthand double-colon <code>hx-on::</code> for htmx
events, and omit the “htmx” part:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span style="font-style:italic;color:#848da1;">&lt;!-- These two are equivalent --&gt;
</span><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/info" </span><span style="color:#d19a66;">hx-on:htmx:before-request</span><span>=</span><span style="color:#98c379;">"alert('Making a request!')"</span><span>&gt;
</span><span>    Get Info!
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>
</span><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/info" </span><span style="color:#d19a66;">hx-on::before-request</span><span>=</span><span style="color:#98c379;">"alert('Making a request!')"</span><span>&gt;
</span><span>    Get Info!
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>
</span></code></pre>If you wish to handle multiple different events, you can simply add multiple attributes to an element:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/info"
</span><span>        </span><span style="color:#d19a66;">hx-on::before-request</span><span>=</span><span style="color:#98c379;">"alert('Making a request!')"
</span><span>        </span><span style="color:#d19a66;">hx-on::after-request</span><span>=</span><span style="color:#98c379;">"alert('Done making a request!')"</span><span>&gt;
</span><span>    Get Info!
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>Finally, in order to make this feature compatible with some templating languages (e.g. <a rel="noopener" target="_blank" href="https://react.dev/learn/writing-markup-with-jsx">JSX</a>) that do not like having a colon (<code>:</code>)
in HTML attributes, you may use dashes in the place of colons for both the long form and the shorthand form:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span style="font-style:italic;color:#848da1;">&lt;!-- These two are equivalent --&gt;
</span><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/info" </span><span style="color:#d19a66;">hx-on-htmx-before-request</span><span>=</span><span style="color:#98c379;">"alert('Making a request!')"</span><span>&gt;
</span><span>    Get Info!
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>
</span><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/info" </span><span style="color:#d19a66;">hx-on--before-request</span><span>=</span><span style="color:#98c379;">"alert('Making a request!')"</span><span>&gt;
</span><span>    Get Info!
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>
</span></code></pre>### hx-on (deprecated)The value is an event name, followed by a colon <code>:</code>, followed by the script:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/info" </span><span style="color:#d19a66;">hx-on</span><span>=</span><span style="color:#98c379;">"htmx:beforeRequest: alert('Making a request!')"</span><span>&gt;
</span><span>    Get Info!
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>Multiple handlers can be defined by putting them on new lines:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/info" </span><span style="color:#d19a66;">hx-on</span><span>=</span><span style="color:#98c379;">"htmx:beforeRequest: alert('Making a request!')
</span><span style="color:#98c379;">                              htmx:afterRequest: alert('Done making a request!')"</span><span>&gt;
</span><span>    Get Info!
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>### SymbolsLike <code>onevent</code>, two symbols are made available to event handler scripts:

- <code>this</code> - The element on which the <code>hx-on</code> attribute is defined
- <code>event</code> - The event that triggered the handler

### Notes- <code>hx-on</code> is <em>not</em> inherited, however due to
<a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_bubbling_and_capture">event bubbling</a>,
<code>hx-on</code> attributes on parent elements will typically be triggered by events on child elements
- <code>hx-on:*</code> and <code>hx-on</code> cannot be used together on the same element; if <code>hx-on:*</code> is present, the value of an <code>hx-on</code> attribute
on the same element will be ignored. The two forms can be mixed in the same document, however.

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# HX-Replace-Url

URL: https://htmx.org/headers/hx-replace-url/

<h1>HX-Replace-Url Response Header</h1>The <code>HX-Replace-Url</code> header allows you to replace the current URL in the browser <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">location history</a>.
This does not create a new history entry; in effect, it removes the previous current URL from the browser’s history.
This is similar to the <a href="https://htmx.org/attributes/hx-replace-url/"><code>hx-replace-url</code> attribute</a>.

If present, this header overrides any behavior defined with attributes.

The possible values for this header are:

<ol>
<li>A URL to replace the current URL in the location bar.
This may be relative or absolute, as per <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState"><code>history.replaceState()</code></a>, but must have the same origin as the current URL.</li>
<li><code>false</code>, which prevents the browser’s current URL from being updated.</li>
</ol><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# HX-Trigger

URL: https://htmx.org/headers/hx-trigger/

<h1>HX-Trigger Response Headers</h1>These response headers can be used to trigger client side actions on the target element within a response to htmx.  You
can trigger a single event or as many uniquely named events as you would like.

The headers are:

- <code>HX-Trigger</code> - trigger events as soon as the response is received.
- <code>HX-Trigger-After-Settle</code> - trigger events after the <a href="https://htmx.org/docs/#request-operations">settling step</a>.
- <code>HX-Trigger-After-Swap</code> - trigger events after the <a href="https://htmx.org/docs/#request-operations">swap step</a>.

To trigger a single event with no additional details you can simply send the event name in a header like so:

<code>HX-Trigger: myEvent</code>

This will trigger <code>myEvent</code> on the triggering element and will bubble up to the body.  As an example you could
listen for this event like this:

<pre data-lang="javascript" style="background-color:#1f2329;color:#abb2bf;" class="language-javascript "><code class="language-javascript" data-lang="javascript"><span>document.body.</span><span style="color:#56b6c2;">addEventListener</span><span>(</span><span style="color:#98c379;">"myEvent"</span><span>, </span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">evt</span><span>){
</span><span>    </span><span style="color:#61afef;">alert</span><span>(</span><span style="color:#98c379;">"myEvent was triggered!"</span><span>);
</span><span>})
</span></code></pre>… or like this, if you’re trying to trigger some element without using JS code:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span style="font-style:italic;color:#848da1;">&lt;!-- Since it bubbles up to the &lt;body&gt;, we must use the `from:body` modifier below --&gt;
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"myEvent from:body" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>If you want to pass details along with the event, you can move to JSON for the value of the trigger:

<code>HX-Trigger: {"showMessage":"Here Is A Message"}</code>

To handle this event you would write the following code:

<pre data-lang="javascript" style="background-color:#1f2329;color:#abb2bf;" class="language-javascript "><code class="language-javascript" data-lang="javascript"><span>document.body.</span><span style="color:#56b6c2;">addEventListener</span><span>(</span><span style="color:#98c379;">"showMessage"</span><span>, </span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">evt</span><span>){
</span><span>    </span><span style="color:#61afef;">alert</span><span>(</span><span style="color:#e06c75;">evt</span><span>.</span><span style="color:#e06c75;">detail</span><span>.value);
</span><span>})
</span></code></pre>Note that the value of the message was put into the <code>detail.value</code> slot.  If you wish to pass multiple pieces of data
you can use a nested JSON object on the right hand side of the JSON object:

<code>HX-Trigger: {"showMessage":{"level" : "info", "message" : "Here Is A Message"}}</code>

And handle this event like so:

<pre data-lang="javascript" style="background-color:#1f2329;color:#abb2bf;" class="language-javascript "><code class="language-javascript" data-lang="javascript"><span>document.body.</span><span style="color:#56b6c2;">addEventListener</span><span>(</span><span style="color:#98c379;">"showMessage"</span><span>, </span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">evt</span><span>){
</span><span>   </span><span style="color:#c678dd;">if</span><span>(</span><span style="color:#e06c75;">evt</span><span>.</span><span style="color:#e06c75;">detail</span><span>.</span><span style="color:#e06c75;">level </span><span>=== </span><span style="color:#98c379;">"info"</span><span>){
</span><span>     </span><span style="color:#61afef;">alert</span><span>(</span><span style="color:#e06c75;">evt</span><span>.</span><span style="color:#e06c75;">detail</span><span>.</span><span style="color:#e06c75;">message</span><span>);   
</span><span>   }
</span><span>})
</span></code></pre>Each property of the JSON object on the right hand side will be copied onto the details object for the event.

### Targetting Other ElementsYou can trigger events on other target elements by adding a <code>target</code> argument to the JSON object.

<code>HX-Trigger: {"showMessage":{"target" : "#otherElement"}}</code>

### Multiple TriggersIf you wish to invoke multiple events, you can simply add additional properties to the top level JSON
object:

<code>HX-Trigger: {"event1":"A message", "event2":"Another message"}</code>

You may also trigger multiple events with no additional details by sending event names separated by commas, like so:

<code>HX-Trigger: event1, event2</code>

Using events gives you a lot of flexibility to add functionality to normal htmx responses.

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# HX-Location

URL: https://htmx.org/headers/hx-location/

<h1>HX-Location Response Header</h1>This response header can be used to trigger a client side redirection without reloading the whole page. Instead of changing the page’s location it will act like following a <a href="https://htmx.org/attributes/hx-boost/"><code>hx-boost</code> link</a>, creating a new history entry, issuing an ajax request to the value of the header and pushing the path into history.

A sample response would be:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>HX-Location: /test
</span></code></pre>Which would push the client to test as if the user had clicked on <code>&lt;a href="/test" hx-boost="true"&gt;</code>

If you want to redirect to a specific target on the page rather than the default of document.body, you can pass more details along with the event, by using JSON for the value of the header:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>HX-Location: {"path":"/test2", "target":"#testdiv"}
</span></code></pre>Path is required and is url to load the response from. The rest of the data mirrors the <a href="https://htmx.org/api/#ajax"><code>ajax</code> api</a> context, which is:

- <code>source</code> - the source element of the request
- <code>event</code> - an event that “triggered” the request
- <code>handler</code> - a callback that will handle the response HTML
- <code>target</code> - the target to swap the response into
- <code>swap</code> - how the response will be swapped in relative to the target
- <code>values</code> - values to submit with the request
- <code>headers</code> - headers to submit with the request
- <code>select</code> - allows you to select the content you want swapped from a response

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-vars

URL: https://htmx.org/attributes/hx-vars/

<h1><code>hx-vars</code></h1><strong>NOTE: <code>hx-vars</code> has been deprecated in favor of <a href="https://htmx.org/attributes/hx-vals/"><code>hx-vals</code></a>, which is safer by default.</strong>

The <code>hx-vars</code> attribute allows you to dynamically add to the parameters that will be submitted with an AJAX request.

The value of this attribute is a comma separated list of <code>name</code>:<code>&lt;expression&gt;</code> values, the same as the internal
syntax of javascript <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Object_literals">Object Literals</a>.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-vars</span><span>=</span><span style="color:#98c379;">"myVar:computeMyVar()"</span><span>&gt;Get Some HTML, Including A Dynamic Value in the Request&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h2 id="security-considerations">Security Considerations</h2>- The expressions in <code>hx-vars</code> are dynamically computed which allows you to add JavaScript code that will be executed. Be careful to <strong>never</strong> trust user input in your expressions as this may lead to a <a rel="noopener" target="_blank" href="https://owasp.org/www-community/attacks/xss/">Cross-Site Scripting (XSS)</a> vulnerability. If you are dealing with user input such as query strings or user-generated content, consider using <a href="https://htmx.org/attributes/hx-vals/">hx-vals</a> which is a safer alternative.

<h2 id="notes">Notes</h2>- <code>hx-vars</code> is inherited and can be placed on a parent element.
- A child declaration of a variable overrides a parent declaration.
- Input values with the same name will be overridden by variable declarations.

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-sync

URL: https://htmx.org/attributes/hx-sync/

<h1><code>hx-sync</code></h1>The <code>hx-sync</code> attribute allows you to synchronize AJAX requests between multiple elements.

The <code>hx-sync</code> attribute consists of a CSS selector to indicate the element to synchronize on, followed optionally
by a colon and then by an optional syncing strategy.  The available strategies are:

- <code>drop</code> - drop (ignore) this request if an existing request is in flight (the default)
- <code>abort</code> - drop (ignore) this request if an existing request is in flight, and, if that is not the case,
<em>abort</em> this request if another request occurs while it is still in flight
- <code>replace</code> - abort the current request, if any, and replace it with this request
- <code>queue</code> - place this request in the request queue associated with the given element

The <code>queue</code> modifier can take an additional argument indicating exactly how to queue:

- <code>queue first</code> - queue the first request to show up while a request is in flight
- <code>queue last</code> - queue the last request to show up while a request is in flight
- <code>queue all</code> - queue all requests that show up while a request is in flight

<h2 id="notes">Notes</h2>- <code>hx-sync</code> is inherited and can be placed on a parent element

This example resolves a race condition between a form’s submit request and an individual input’s validation request. Normally, without using <code>hx-sync</code>, filling out the input and immediately submitting the form triggers two parallel requests to <code>/validate</code> and <code>/store</code>. Using <code>hx-sync="closest form:abort"</code> on the input will watch for requests on the form and abort the input’s request if a form request is present or starts while the input request is in flight.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/store"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"title" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"title" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text" 
</span><span>        </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/validate" 
</span><span>        </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"change"
</span><span>        </span><span style="color:#d19a66;">hx-sync</span><span>=</span><span style="color:#98c379;">"closest form:abort"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"submit"</span><span>&gt;Submit&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>If you’d rather prioritize the validation request over the submit request, you can use the <code>drop</code> strategy. This example will prioritize the validation request over the submit request so that if a validation request is in flight, the form cannot be submitted.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/store"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"title" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"title" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text" 
</span><span>        </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/validate" 
</span><span>        </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"change"
</span><span>        </span><span style="color:#d19a66;">hx-sync</span><span>=</span><span style="color:#98c379;">"closest form:drop"
</span><span>    &gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"submit"</span><span>&gt;Submit&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>When dealing with forms that contain many inputs, you can prioritize the submit request over all input validation requests using the hx-sync <code>replace</code> strategy on the form tag. This will cancel any in-flight validation requests and issue only the <code>hx-post="/store"</code> request. If you’d rather abort the submit request and prioritize any existing validation requests you can use the <code>hx-sync="this:abort"</code> strategy on the form tag.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/store" </span><span style="color:#d19a66;">hx-sync</span><span>=</span><span style="color:#98c379;">"this:replace"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"title" </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"title" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text" </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/validate" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"change" </span><span>/&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"submit"</span><span>&gt;Submit&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>When implementing active search functionality the hx-trigger attribute’s <code>delay</code> modifier can be used to debounce the user’s input and avoid making multiple requests while the user types. However, once a request is made, if the user begins typing again a new request will begin even if the previous one has not finished processing. This example will cancel any in-flight requests and use only the last request. In cases where the search input is contained within the target, then using <code>hx-sync</code> like this also helps reduce the chances that the input will be replaced while the user is still typing.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"search" 
</span><span>    </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/search" 
</span><span>    </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"keyup changed delay:500ms, search" 
</span><span>    </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#search-results"
</span><span>    </span><span style="color:#d19a66;">hx-sync</span><span>=</span><span style="color:#98c379;">"this:replace"</span><span>&gt;
</span></code></pre><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-request

URL: https://htmx.org/attributes/hx-request/

<h1><code>hx-request</code></h1>The <code>hx-request</code> attribute allows you to configure various aspects of the request via the following attributes:

- <code>timeout</code> - the timeout for the request, in milliseconds
- <code>credentials</code> - if the request will send credentials
- <code>noHeaders</code> - strips all headers from the request

These attributes are set using a JSON-like syntax:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">... hx-request</span><span>=</span><span style="color:#98c379;">'{"timeout":100}'</span><span>&gt;
</span><span>  ...
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>You may make the values dynamically evaluated by adding the <code>javascript:</code> or <code>js:</code> prefix:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">... hx-request</span><span>=</span><span style="color:#98c379;">'js: timeout:getTimeoutSetting() '</span><span>&gt;
</span><span>  ...
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h2 id="notes">Notes</h2>- <code>hx-request</code> is merge-inherited and can be placed on a parent element

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-replace-url

URL: https://htmx.org/attributes/hx-replace-url/

<h1><code>hx-replace-url</code></h1>The <code>hx-replace-url</code> attribute allows you to replace the current url of the browser <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">location history</a>.

The possible values of this attribute are:

<ol>
<li><code>true</code>, which replaces the fetched URL in the browser navigation bar.</li>
<li><code>false</code>, which disables replacing the fetched URL if it would otherwise be replaced due to inheritance.</li>
<li>A URL to be replaced into the location bar.
This may be relative or absolute, as per <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState"><code>history.replaceState()</code></a>.</li>
</ol>Here is an example:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/account" </span><span style="color:#d19a66;">hx-replace-url</span><span>=</span><span style="color:#98c379;">"true"</span><span>&gt;
</span><span>  Go to My Account
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This will cause htmx to snapshot the current DOM to <code>localStorage</code> and replace the URL `/account’ in the browser location bar.

Another example:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/account" </span><span style="color:#d19a66;">hx-replace-url</span><span>=</span><span style="color:#98c379;">"/account/home"</span><span>&gt;
</span><span>  Go to My Account
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This will replace the URL `/account/home’ in the browser location bar.

<h2 id="notes">Notes</h2>- <code>hx-replace-url</code> is inherited and can be placed on a parent element
- The <a href="https://htmx.org/headers/hx-replace-url/"><code>HX-Replace-Url</code> response header</a> has similar behavior and can override this attribute.
- The <a href="https://htmx.org/attributes/hx-history-elt/"><code>hx-history-elt</code> attribute</a> allows changing which element is saved in the history cache.
- The <a href="https://htmx.org/attributes/hx-push-url/"><code>hx-push-url</code> attribute</a> is a similar and more commonly used attribute, which creates a
new history entry rather than replacing the current one.

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-validate

URL: https://htmx.org/attributes/hx-validate/

<h1><code>hx-validate</code></h1>The <code>hx-validate</code> attribute will cause an element to validate itself by way of the <a href="https://htmx.org/docs/#validation">HTML5 Validation API</a>
before it submits a request.

Only <code>&lt;form&gt;</code> elements validate data by default, but other elements do not. Adding <code>hx-validate="true"</code> to <code>&lt;input&gt;</code>, <code>&lt;textarea&gt;</code> or <code>&lt;select&gt;</code> enables validation before sending requests.

<h2 id="notes">Notes</h2>- <code>hx-validate</code> is not inherited

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-put

URL: https://htmx.org/attributes/hx-put/

<h1><code>hx-put</code></h1>The <code>hx-put</code> attribute will cause an element to issue a <code>PUT</code> to the specified URL and swap
the HTML into the DOM using a swap strategy:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-put</span><span>=</span><span style="color:#98c379;">"/account" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"body"</span><span>&gt;
</span><span>  Put Money In Your Account
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>This example will cause the <code>button</code> to issue a <code>PUT</code> to <code>/account</code> and swap the returned HTML into
the <code>innerHTML</code> of the <code>body</code>.

<h2 id="notes">Notes</h2>- <code>hx-put</code> is not inherited
- You can control the target of the swap using the <a href="https://htmx.org/attributes/hx-target/">hx-target</a> attribute
- You can control the swap strategy by using the <a href="https://htmx.org/attributes/hx-swap/">hx-swap</a> attribute
- You can control what event triggers the request with the <a href="https://htmx.org/attributes/hx-trigger/">hx-trigger</a> attribute
- You can control the data submitted with the request in various ways, documented here: <a href="https://htmx.org/docs/#parameters">Parameters</a>

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-prompt

URL: https://htmx.org/attributes/hx-prompt/

<h1><code>hx-prompt</code></h1>The <code>hx-prompt</code> attribute allows you to show a prompt before issuing a request.  The value of
the prompt will be included in the request in the <code>HX-Prompt</code> header.

Here is an example:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-delete</span><span>=</span><span style="color:#98c379;">"/account" </span><span style="color:#d19a66;">hx-prompt</span><span>=</span><span style="color:#98c379;">"Enter your account name to confirm deletion"</span><span>&gt;
</span><span>  Delete My Account
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre><h2 id="notes">Notes</h2>- <code>hx-prompt</code> is inherited and can be placed on a parent element

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# htmx:abort

URL: https://htmx.org/events/

<h1>Events</h1>Htmx provides an extensive events system that can be used to modify and enhance behavior.  Events
are listed below.

### <a class="zola-anchor" href="#htmx:abort" aria-label="Anchor link for: htmx:abort">#</a>Event - <code>htmx:abort</code>This event is different than other events: htmx does not <em>trigger</em> it, but rather <em>listens</em> for it.

If you send an <code>htmx:abort</code> event to an element making a request, it will abort the request:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"request-button" </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/example"</span><span>&gt;Issue Request&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">onclick</span><span>=</span><span style="color:#98c379;">"</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#e06c75;">trigger</span><span>(</span><span style="color:#98c379;">'#request-button'</span><span>, </span><span style="color:#98c379;">'htmx:abort'</span><span>)</span><span style="color:#98c379;">"</span><span>&gt;Cancel Request&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>### <a class="zola-anchor" href="#htmx:afterOnLoad" aria-label="Anchor link for: htmx:afterOnLoad">#</a>Event - <code>htmx:afterOnLoad</code>This event is triggered after an AJAX <code>onload</code> has finished.  Note that this does not mean that the content
has been swapped or settled yet, only that the request has finished.

<h5 id="details"><a class="zola-anchor" href="#details" aria-label="Anchor link for: details">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:afterProcessNode" aria-label="Anchor link for: htmx:afterProcessNode">#</a>Event - <code>htmx:afterProcessNode</code>This event is triggered after htmx has initialized a DOM node.  It can be useful for extensions to build additional features onto a node.

<h5 id="details-1"><a class="zola-anchor" href="#details-1" aria-label="Anchor link for: details-1">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request

### <a class="zola-anchor" href="#htmx:afterRequest" aria-label="Anchor link for: htmx:afterRequest">#</a>Event - <code>htmx:afterRequest</code>This event is triggered after an AJAX request has finished either in the case of a successful request (although
one that may have returned a remote error code such as a <code>404</code>) or in a network error situation.  This event
can be paired with <a href="https://htmx.org/events/#htmx:beforeRequest"><code>htmx:beforeRequest</code></a> to wrap behavior around a request cycle.

<h5 id="details-2"><a class="zola-anchor" href="#details-2" aria-label="Anchor link for: details-2">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request
- <code>detail.successful</code> - true if the response has a 20x status code or is marked <code>detail.isError = false</code> in the
<code>htmx:beforeSwap</code> event, else false
- <code>detail.failed</code> - true if the response does not have a 20x status code or is marked <code>detail.isError = true</code> in the
<code>htmx:beforeSwap</code> event, else false

### <a class="zola-anchor" href="#htmx:afterSettle" aria-label="Anchor link for: htmx:afterSettle">#</a>Event - <code>htmx:afterSettle</code>This event is triggered after the DOM has <a href="https://htmx.org/docs/#request-operations">settled</a>.

<h5 id="details-3"><a class="zola-anchor" href="#details-3" aria-label="Anchor link for: details-3">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:afterSwap" aria-label="Anchor link for: htmx:afterSwap">#</a>Event - <code>htmx:afterSwap</code>This event is triggered after new content has been <a href="https://htmx.org/docs/#swapping">swapped into the DOM</a>.

<h5 id="details-4"><a class="zola-anchor" href="#details-4" aria-label="Anchor link for: details-4">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:beforeCleanupElement" aria-label="Anchor link for: htmx:beforeCleanupElement">#</a>Event - <code>htmx:beforeCleanupElement</code>This event is triggered before htmx <a href="https://htmx.org/attributes/hx-disable/">disables</a> an element or removes it from the DOM.

<h5 id="details-5"><a class="zola-anchor" href="#details-5" aria-label="Anchor link for: details-5">#</a>Details</h5>- <code>detail.elt</code> - the cleaned up element

### <a class="zola-anchor" href="#htmx:beforeOnLoad" aria-label="Anchor link for: htmx:beforeOnLoad">#</a>Event - <code>htmx:beforeOnLoad</code>This event is triggered before any response processing occurs.  If the event is cancelled, no swap will occur.

<h5 id="details-6"><a class="zola-anchor" href="#details-6" aria-label="Anchor link for: details-6">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:beforeProcessNode" aria-label="Anchor link for: htmx:beforeProcessNode">#</a>Event - <code>htmx:beforeProcessNode</code>This event is triggered before htmx initializes a DOM node and has processed all of its <code>hx-</code> attributes.  This gives extensions and other external code the ability to modify the contents of a DOM node before it is processed.

<h5 id="details-7"><a class="zola-anchor" href="#details-7" aria-label="Anchor link for: details-7">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request

### <a class="zola-anchor" href="#htmx:beforeRequest" aria-label="Anchor link for: htmx:beforeRequest">#</a>Event - <code>htmx:beforeRequest</code>This event is triggered before an AJAX request is issued.  If the event is cancelled, no request will occur.

<h5 id="details-8"><a class="zola-anchor" href="#details-8" aria-label="Anchor link for: details-8">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:beforeSend" aria-label="Anchor link for: htmx:beforeSend">#</a>Event - <code>htmx:beforeSend</code>This event is triggered right before a request is sent.  You may not cancel the request with this event.

<h5 id="details-9"><a class="zola-anchor" href="#details-9" aria-label="Anchor link for: details-9">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:beforeSwap" aria-label="Anchor link for: htmx:beforeSwap">#</a>Event - <code>htmx:beforeSwap</code>This event is triggered before any new content has been <a href="https://htmx.org/docs/#swapping">swapped into the DOM</a>.  If the event is cancelled, no swap will occur.

You can modify the default swap behavior by modifying the <code>shouldSwap</code> and <code>target</code> properties of the event detail. See
the documentation on <a href="https://htmx.org/docs/#modifying_swapping_behavior_with_events">configuring swapping</a> for more details.

<h5 id="details-10"><a class="zola-anchor" href="#details-10" aria-label="Anchor link for: details-10">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.requestConfig</code> - the configuration of the AJAX request
- <code>detail.shouldSwap</code> - if the content will be swapped (defaults to <code>false</code> for non-200 response codes)
- <code>detail.ignoreTitle</code> - if <code>true</code> any title tag in the response will be ignored
- <code>detail.target</code> - the target of the swap

### <a class="zola-anchor" href="#htmx:beforeTransition" aria-label="Anchor link for: htmx:beforeTransition">#</a>Event - <code>htmx:beforeTransition</code>This event is triggered before a <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API">View Transition</a>
wrapped swap occurs.  If the event is cancelled, the View Transition will not occur and the normal swapping logic will
happen instead.

<h5 id="details-11"><a class="zola-anchor" href="#details-11" aria-label="Anchor link for: details-11">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.requestConfig</code> - the configuration of the AJAX request
- <code>detail.shouldSwap</code> - if the content will be swapped (defaults to <code>false</code> for non-200 response codes)
- <code>detail.target</code> - the target of the swap

### <a class="zola-anchor" href="#htmx:configRequest" aria-label="Anchor link for: htmx:configRequest">#</a>Event - <code>htmx:configRequest</code>This event is triggered after htmx has collected parameters for inclusion in the request.  It can be
used to include or update the parameters that htmx will send:

<pre data-lang="javascript" style="background-color:#1f2329;color:#abb2bf;" class="language-javascript "><code class="language-javascript" data-lang="javascript"><span>document.body.</span><span style="color:#56b6c2;">addEventListener</span><span>(</span><span style="color:#98c379;">'htmx:configRequest'</span><span>, </span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">evt</span><span>) {
</span><span>    </span><span style="color:#e06c75;">evt</span><span>.</span><span style="color:#e06c75;">detail</span><span>.</span><span style="color:#e06c75;">parameters</span><span>[</span><span style="color:#98c379;">'auth_token'</span><span>] = </span><span style="color:#61afef;">getAuthToken</span><span>(); </span><span style="font-style:italic;color:#848da1;">// add a new parameter into the mix
</span><span>});
</span></code></pre>Note that if an input value appears more than once the value in the <code>parameters</code> object will be an array, rather
than a single value.

<h5 id="details-12"><a class="zola-anchor" href="#details-12" aria-label="Anchor link for: details-12">#</a>Details</h5>- <code>detail.parameters</code> - the parameters that will be submitted in the request
- <code>detail.unfilteredParameters</code> - the parameters that were found before filtering by <a href="https://htmx.org/attributes/hx-select/"><code>hx-select</code></a>
- <code>detail.headers</code> - the request headers
- <code>detail.elt</code> - the element that triggered the request
- <code>detail.target</code> - the target of the request
- <code>detail.verb</code> - the HTTP verb in use

### <a class="zola-anchor" href="#htmx:confirm" aria-label="Anchor link for: htmx:confirm">#</a>Event - <code>htmx:confirm</code>This event is triggered immediately after a trigger occurs on an element.  It allows you to cancel (or delay) issuing
the AJAX request.  If you call <code>preventDefault()</code> on the event, it will not issue the given request.  The <code>detail</code>
object contains a function, <code>evt.detail.issueRequest()</code>, that can be used to issue the actual AJAX request at a
later point.  Combining these two features allows you to create an asynchronous confirmation dialog.

Here is an example using <a rel="noopener" target="_blank" href="https://sweetalert.js.org/guides/">sweet alert</a> on any element with a <code>confirm-with-sweet-alert='true'</code> attribute on it:

<pre data-lang="javascript" style="background-color:#1f2329;color:#abb2bf;" class="language-javascript "><code class="language-javascript" data-lang="javascript"><span>document.body.</span><span style="color:#56b6c2;">addEventListener</span><span>(</span><span style="color:#98c379;">'htmx:confirm'</span><span>, </span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">evt</span><span>) {
</span><span>  </span><span style="color:#c678dd;">if </span><span>(</span><span style="color:#e06c75;">evt</span><span>.target.</span><span style="color:#56b6c2;">matches</span><span>(</span><span style="color:#98c379;">"[confirm-with-sweet-alert='true']"</span><span>)) {
</span><span>    </span><span style="color:#e06c75;">evt</span><span>.</span><span style="color:#56b6c2;">preventDefault</span><span>();
</span><span>    </span><span style="color:#61afef;">swal</span><span>({
</span><span>      title: </span><span style="color:#98c379;">"Are you sure?"</span><span>,
</span><span>      text: </span><span style="color:#98c379;">"Are you sure you are sure?"</span><span>,
</span><span>      icon: </span><span style="color:#98c379;">"warning"</span><span>,
</span><span>      buttons: </span><span style="color:#d19a66;">true</span><span>,
</span><span>      dangerMode: </span><span style="color:#d19a66;">true</span><span>,
</span><span>    }).</span><span style="color:#56b6c2;">then</span><span>((</span><span style="color:#e06c75;">confirmed</span><span>) </span><span style="color:#c678dd;">=&gt; </span><span>{
</span><span>      </span><span style="color:#c678dd;">if </span><span>(</span><span style="color:#e06c75;">confirmed</span><span>) {
</span><span>        </span><span style="color:#e06c75;">evt</span><span>.</span><span style="color:#e06c75;">detail</span><span>.</span><span style="color:#61afef;">issueRequest</span><span>();
</span><span>      }
</span><span>    });
</span><span>  }
</span><span>});
</span></code></pre><h5 id="details-13"><a class="zola-anchor" href="#details-13" aria-label="Anchor link for: details-13">#</a>Details</h5>{target: target, elt: elt, path: path, verb: verb, triggeringEvent: event, etc: etc, issueRequest: issueRequest}

- <code>detail.elt</code> - the element in question
- <code>detail.etc</code> - additional request information (mostly unused)
- <code>detail.issueRequest</code> - a no argument function that can be invoked to issue the request (should be paired with <code>evt.preventDefault()</code>!)
- <code>detail.path</code> - the path of the request
- <code>detail.target</code> - the target of the request
- <code>detail.triggeringEvent</code> - the original event that triggered this request
- <code>detail.verb</code> - the verb of the request (e.g. <code>GET</code>)

### <a class="zola-anchor" href="#htmx:historyCacheError" aria-label="Anchor link for: htmx:historyCacheError">#</a>Event - <code>htmx:historyCacheError</code>This event is triggered when an attempt to save the cache to <code>localStorage</code> fails

<h5 id="details-14"><a class="zola-anchor" href="#details-14" aria-label="Anchor link for: details-14">#</a>Details</h5>- <code>detail.cause</code> - the <code>Exception</code> that was thrown when attempting to save history to <code>localStorage</code>

### <a class="zola-anchor" href="#htmx:historyCacheMiss" aria-label="Anchor link for: htmx:historyCacheMiss">#</a>Event - <code>htmx:historyCacheMiss</code>This event is triggered when a cache miss occurs when restoring history

<h5 id="details-15"><a class="zola-anchor" href="#details-15" aria-label="Anchor link for: details-15">#</a>Details</h5>- <code>detail.xhr</code> - the <code>XMLHttpRequest</code> that will retrieve the remote content for restoration
- <code>detail.path</code> - the path and query of the page being restored

### <a class="zola-anchor" href="#htmx:historyCacheMissError" aria-label="Anchor link for: htmx:historyCacheMissError">#</a>Event - <code>htmx:historyCacheMissError</code>This event is triggered when a cache miss occurs and a response has been retrieved from the server
for the content to restore, but the response is an error (e.g. <code>404</code>)

<h5 id="details-16"><a class="zola-anchor" href="#details-16" aria-label="Anchor link for: details-16">#</a>Details</h5>- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.path</code> - the path and query of the page being restored

### <a class="zola-anchor" href="#htmx:historyCacheMissLoad" aria-label="Anchor link for: htmx:historyCacheMissLoad">#</a>Event - <code>htmx:historyCacheMissLoad</code>This event is triggered when a cache miss occurs and a response has been retrieved successfully from the server
for the content to restore

<h5 id="details-17"><a class="zola-anchor" href="#details-17" aria-label="Anchor link for: details-17">#</a>Details</h5>- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.path</code> - the path and query of the page being restored

### <a class="zola-anchor" href="#htmx:historyRestore" aria-label="Anchor link for: htmx:historyRestore">#</a>Event - <code>htmx:historyRestore</code>This event is triggered when htmx handles a history restoration action

<h5 id="details-18"><a class="zola-anchor" href="#details-18" aria-label="Anchor link for: details-18">#</a>Details</h5>- <code>detail.path</code> - the path and query of the page being restored

### <a class="zola-anchor" href="#htmx:beforeHistorySave" aria-label="Anchor link for: htmx:beforeHistorySave">#</a>Event - <code>htmx:beforeHistorySave</code>This event is triggered before the content is saved in the history api.

<h5 id="details-19"><a class="zola-anchor" href="#details-19" aria-label="Anchor link for: details-19">#</a>Details</h5>- <code>detail.path</code> - the path and query of the page being restored
- <code>detail.historyElt</code> - the history element being restored into

<h5 id="details-20"><a class="zola-anchor" href="#details-20" aria-label="Anchor link for: details-20">#</a>Details</h5>- <code>detail.config</code> - the config that will be passed to the <code>EventSource</code> constructor

### <a class="zola-anchor" href="#htmx:load" aria-label="Anchor link for: htmx:load">#</a>Event - <code>htmx:load</code>This event is triggered when a new node is loaded into the DOM by htmx.

<h5 id="details-21"><a class="zola-anchor" href="#details-21" aria-label="Anchor link for: details-21">#</a>Details</h5>- <code>detail.elt</code> - the newly added element

### <a class="zola-anchor" href="#htmx:noSSESourceError" aria-label="Anchor link for: htmx:noSSESourceError">#</a>Event - <code>htmx:noSSESourceError</code>This event is triggered when an element refers to an SSE event in its trigger, but no parent SSE source has been defined

<h5 id="details-22"><a class="zola-anchor" href="#details-22" aria-label="Anchor link for: details-22">#</a>Details</h5>- <code>detail.elt</code> - the element with the bad SSE trigger

### <a class="zola-anchor" href="#htmx:oobAfterSwap" aria-label="Anchor link for: htmx:oobAfterSwap">#</a>Event - <code>htmx:oobAfterSwap</code>This event is triggered as part of an <a href="https://htmx.org/docs/#oob_swaps">out of band swap</a> and behaves identically to an <a href="https://htmx.org/events/#htmx:afterSwap">after swap event</a>

<h5 id="details-23"><a class="zola-anchor" href="#details-23" aria-label="Anchor link for: details-23">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.shouldSwap</code> - if the content will be swapped (defaults to <code>true</code>)
- <code>detail.target</code> - the target of the swap
- <code>detail.fragment</code> - the response fragment

### <a class="zola-anchor" href="#htmx:oobBeforeSwap" aria-label="Anchor link for: htmx:oobBeforeSwap">#</a>Event - <code>htmx:oobBeforeSwap</code>This event is triggered as part of an <a href="https://htmx.org/docs/#oob_swaps">out of band swap</a> and behaves identically to a <a href="https://htmx.org/events/#htmx:beforeSwap">before swap event</a>

<h5 id="details-24"><a class="zola-anchor" href="#details-24" aria-label="Anchor link for: details-24">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.shouldSwap</code> - if the content will be swapped (defaults to <code>true</code>)
- <code>detail.target</code> - the target of the swap
- <code>detail.fragment</code> - the response fragment

### <a class="zola-anchor" href="#htmx:oobErrorNoTarget" aria-label="Anchor link for: htmx:oobErrorNoTarget">#</a>Event - <code>htmx:oobErrorNoTarget</code>This event is triggered when an <a href="https://htmx.org/docs/#oob_swaps">out of band swap</a> does not have a corresponding element
in the DOM to switch with.

<h5 id="details-25"><a class="zola-anchor" href="#details-25" aria-label="Anchor link for: details-25">#</a>Details</h5>- <code>detail.content</code> - the element with the bad oob <code>id</code>

### <a class="zola-anchor" href="#htmx:onLoadError" aria-label="Anchor link for: htmx:onLoadError">#</a>Event - <code>htmx:onLoadError</code>This event is triggered when an error occurs during the <code>load</code> handling of an AJAX call

<h5 id="details-26"><a class="zola-anchor" href="#details-26" aria-label="Anchor link for: details-26">#</a>Details</h5>- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.elt</code> - the element that triggered the request
- <code>detail.target</code> - the target of the request
- <code>detail.exception</code> - the exception that occurred
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:prompt" aria-label="Anchor link for: htmx:prompt">#</a>Event - <code>htmx:prompt</code>This event is triggered after a prompt has been shown to the user with the <a href="https://htmx.org/attributes/hx-prompt/"><code>hx-prompt</code></a>
attribute.  If this event is cancelled, the AJAX request will not occur.

<h5 id="details-27"><a class="zola-anchor" href="#details-27" aria-label="Anchor link for: details-27">#</a>Details</h5>- <code>detail.elt</code> - the element that triggered the request
- <code>detail.target</code> - the target of the request
- <code>detail.prompt</code> - the user response to the prompt

### <a class="zola-anchor" href="#htmx:beforeHistoryUpdate" aria-label="Anchor link for: htmx:beforeHistoryUpdate">#</a>Event - <code>htmx:beforeHistoryUpdate</code>This event is triggered before a history update is performed. It can be
used to modify the <code>path</code> or <code>type</code> used to update the history.

<h5 id="details-28"><a class="zola-anchor" href="#details-28" aria-label="Anchor link for: details-28">#</a>Details</h5>- <code>detail.history</code> - the <code>path</code> and <code>type</code> (push, replace) for the history update
- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:pushedIntoHistory" aria-label="Anchor link for: htmx:pushedIntoHistory">#</a>Event - <code>htmx:pushedIntoHistory</code>This event is triggered after a URL has been pushed into history.

<h5 id="details-29"><a class="zola-anchor" href="#details-29" aria-label="Anchor link for: details-29">#</a>Details</h5>- <code>detail.path</code> - the path and query of the URL that has been pushed into history

### <a class="zola-anchor" href="#htmx:replacedInHistory" aria-label="Anchor link for: htmx:replacedInHistory">#</a>Event - <code>htmx:replacedInHistory</code>This event is triggered after a URL has been replaced in history.

<h5 id="details-30"><a class="zola-anchor" href="#details-30" aria-label="Anchor link for: details-30">#</a>Details</h5>- <code>detail.path</code> - the path and query of the URL that has been replaced in history

### <a class="zola-anchor" href="#htmx:responseError" aria-label="Anchor link for: htmx:responseError">#</a>Event - <code>htmx:responseError</code>This event is triggered when an HTTP error response occurs

<h5 id="details-31"><a class="zola-anchor" href="#details-31" aria-label="Anchor link for: details-31">#</a>Details</h5>- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.elt</code> - the element that triggered the request
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:sendError" aria-label="Anchor link for: htmx:sendError">#</a>Event - <code>htmx:sendError</code>This event is triggered when a network error prevents an HTTP request from occurring

<h5 id="details-32"><a class="zola-anchor" href="#details-32" aria-label="Anchor link for: details-32">#</a>Details</h5>- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.elt</code> - the element that triggered the request
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:sseError" aria-label="Anchor link for: htmx:sseError">#</a>Event - <code>htmx:sseError</code>This event is triggered when an error occurs with an SSE source

<h5 id="details-33"><a class="zola-anchor" href="#details-33" aria-label="Anchor link for: details-33">#</a>Details</h5>- <code>detail.elt</code> - the element with the bad SSE source
- <code>detail.error</code> - the error
- <code>detail.source</code> - the SSE source

### <a class="zola-anchor" href="#htmx:swapError" aria-label="Anchor link for: htmx:swapError">#</a>Event - <code>htmx:swapError</code>This event is triggered when an error occurs during the swap phase

<h5 id="details-34"><a class="zola-anchor" href="#details-34" aria-label="Anchor link for: details-34">#</a>Details</h5>- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.elt</code> - the element that triggered the request
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:targetError" aria-label="Anchor link for: htmx:targetError">#</a>Event - <code>htmx:targetError</code>This event is triggered when a bad selector is used for a <a href="https://htmx.org/attributes/hx-target/"><code>hx-target</code></a> attribute (e.g. an
element ID without a preceding <code>#</code>)

<h5 id="details-35"><a class="zola-anchor" href="#details-35" aria-label="Anchor link for: details-35">#</a>Details</h5>- <code>detail.elt</code> - the element that triggered the request
- <code>detail.target</code> - the bad CSS selector

### <a class="zola-anchor" href="#htmx:timeout" aria-label="Anchor link for: htmx:timeout">#</a>Event - <code>htmx:timeout</code>This event is triggered when a request timeout occurs.  This wraps the typical <code>timeout</code> event of XMLHttpRequest.

Timeout time can be set using <code>htmx.config.timeout</code> or per element using <a href="https://htmx.org/attributes/hx-request/"><code>hx-request</code></a>

<h5 id="details-36"><a class="zola-anchor" href="#details-36" aria-label="Anchor link for: details-36">#</a>Details</h5>- <code>detail.elt</code> - the element that dispatched the request
- <code>detail.xhr</code> - the <code>XMLHttpRequest</code>
- <code>detail.target</code> - the target of the request
- <code>detail.requestConfig</code> - the configuration of the AJAX request

### <a class="zola-anchor" href="#htmx:trigger" aria-label="Anchor link for: htmx:trigger">#</a>Event - <code>htmx:trigger</code>This event is triggered whenever an AJAX request would be, even if no AJAX request is specified. It
is primarily intended to allow <code>hx-trigger</code> to execute client-side scripts; AJAX requests have more
granular events available, like <a href="https://htmx.org/events/#htmx:beforeRequest"><code>htmx:beforeRequest</code></a> or <a href="https://htmx.org/events/#htmx:afterRequest"><code>htmx:afterRequest</code></a>.

<h5 id="details-37"><a class="zola-anchor" href="#details-37" aria-label="Anchor link for: details-37">#</a>Details</h5>- <code>detail.elt</code> - the element that triggered the request

### <a class="zola-anchor" href="#htmx:validateUrl" aria-label="Anchor link for: htmx:validateUrl">#</a>Event - <code>htmx:validateUrl</code>This event is triggered before a request is made, allowing you to validate the URL that htmx is going to request.  If
<code>preventDefault()</code> is invoked on the event, the request will not be made.

<pre data-lang="javascript" style="background-color:#1f2329;color:#abb2bf;" class="language-javascript "><code class="language-javascript" data-lang="javascript"><span>document.body.</span><span style="color:#56b6c2;">addEventListener</span><span>(</span><span style="color:#98c379;">'htmx:validateUrl'</span><span>, </span><span style="color:#c678dd;">function </span><span>(</span><span style="color:#e06c75;">evt</span><span>) {
</span><span>  </span><span style="font-style:italic;color:#848da1;">// only allow requests to the current server as well as myserver.com
</span><span>  </span><span style="color:#c678dd;">if </span><span>(!</span><span style="color:#e06c75;">evt</span><span>.</span><span style="color:#e06c75;">detail</span><span>.</span><span style="color:#e06c75;">sameHost </span><span>&amp;&amp; </span><span style="color:#e06c75;">evt</span><span>.</span><span style="color:#e06c75;">detail</span><span>.</span><span style="color:#e06c75;">url</span><span>.hostname !== </span><span style="color:#98c379;">"myserver.com"</span><span>) {
</span><span>    </span><span style="color:#e06c75;">evt</span><span>.</span><span style="color:#56b6c2;">preventDefault</span><span>();
</span><span>  }
</span><span>});
</span></code></pre><h5 id="details-38"><a class="zola-anchor" href="#details-38" aria-label="Anchor link for: details-38">#</a>Details</h5>- <code>detail.elt</code> - the element that triggered the request
- <code>detail.url</code> - the URL Object representing the URL that a request will be sent to.
- <code>detail.sameHost</code> - will be <code>true</code> if the request is to the same host as the document

### <a class="zola-anchor" href="#htmx:validation:validate" aria-label="Anchor link for: htmx:validation:validate">#</a>Event - <code>htmx:validation:validate</code>This event is triggered before an element is validated.  It can be used with the <code>elt.setCustomValidity()</code> method
to implement custom validation rules.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/test"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">_</span><span>=</span><span style="color:#98c379;">"on htmx:validation:validate
</span><span style="color:#98c379;">               if my.value != 'foo'
</span><span style="color:#98c379;">                  call me.setCustomValidity('Please enter the value foo')
</span><span style="color:#98c379;">               else
</span><span style="color:#98c379;">                  call me.setCustomValidity('')"
</span><span>         </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"example"</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre><h5 id="details-39"><a class="zola-anchor" href="#details-39" aria-label="Anchor link for: details-39">#</a>Details</h5>- <code>detail.elt</code> - the element that triggered the request

### <a class="zola-anchor" href="#htmx:validation:failed" aria-label="Anchor link for: htmx:validation:failed">#</a>Event - <code>htmx:validation:failed</code>This event is triggered when an element fails validation.

<h5 id="details-40"><a class="zola-anchor" href="#details-40" aria-label="Anchor link for: details-40">#</a>Details</h5>- <code>detail.elt</code> - the element that triggered the request
- <code>detail.message</code> - the validation error message
- <code>detail.validity</code> - the validity object, which contains properties specifying how validation failed

### <a class="zola-anchor" href="#htmx:validation:halted" aria-label="Anchor link for: htmx:validation:halted">#</a>Event - <code>htmx:validation:halted</code>This event is triggered when a request is halted due to validation errors.

<h5 id="details-41"><a class="zola-anchor" href="#details-41" aria-label="Anchor link for: details-41">#</a>Details</h5>- <code>detail.elt</code> - the element that triggered the request
- <code>detail.errors</code> - an array of error objects with the invalid elements and errors associated with them

### <a class="zola-anchor" href="#htmx:xhr:abort" aria-label="Anchor link for: htmx:xhr:abort">#</a>Event - <code>htmx:xhr:abort</code>This event is triggered when an ajax request aborts

<h5 id="details-42"><a class="zola-anchor" href="#details-42" aria-label="Anchor link for: details-42">#</a>Details</h5>- <code>detail.elt</code> - the element that triggered the request

### <a class="zola-anchor" href="#htmx:xhr:loadstart" aria-label="Anchor link for: htmx:xhr:loadstart">#</a>Event - <code>htmx:xhr:loadstart</code>This event is triggered when an ajax request starts

<h5 id="details-43"><a class="zola-anchor" href="#details-43" aria-label="Anchor link for: details-43">#</a>Details</h5>- <code>detail.elt</code> - the element that triggered the request

### <a class="zola-anchor" href="#htmx:xhr:loadend" aria-label="Anchor link for: htmx:xhr:loadend">#</a>Event - <code>htmx:xhr:loadend</code>This event is triggered when an ajax request finishes

<h5 id="details-44"><a class="zola-anchor" href="#details-44" aria-label="Anchor link for: details-44">#</a>Details</h5>- <code>detail.elt</code> - the element that triggered the request

### <a class="zola-anchor" href="#htmx:xhr:progress" aria-label="Anchor link for: htmx:xhr:progress">#</a>Event - <code>htmx:xhr:progress</code>This event is triggered periodically when an ajax request that supports progress is in flight

<h5 id="details-45"><a class="zola-anchor" href="#details-45" aria-label="Anchor link for: details-45">#</a>Details</h5>- <code>detail.elt</code> - the element that triggered the request

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-preserve

URL: https://htmx.org/attributes/hx-preserve/

<h1><code>hx-preserve</code></h1>The <code>hx-preserve</code> attribute allows you to keep an element unchanged during HTML replacement.
Elements with <code>hx-preserve</code> set are preserved by <code>id</code> when htmx updates any ancestor element.
You <em>must</em> set an unchanging <code>id</code> on elements for <code>hx-preserve</code> to work.
The response requires an element with the same <code>id</code>, but its type and other attributes are ignored.

Note that some elements cannot unfortunately be preserved properly, such as <code>&lt;input type="text"&gt;</code> (focus and caret position are lost), iframes or certain types of videos. To tackle some of these cases we recommend the <a rel="noopener" target="_blank" href="https://github.com/bigskysoftware/htmx-extensions/blob/main/src/morphdom-swap/README.md">morphdom extension</a>, which does a more elaborate DOM
reconciliation.

<h2 id="notes">Notes</h2>- <code>hx-preserve</code> is not inherited

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-params

URL: https://htmx.org/attributes/hx-params/

<h1><code>hx-params</code></h1>The <code>hx-params</code> attribute allows you to filter the parameters that will be submitted with an AJAX request.

The possible values of this attribute are:

- <code>*</code> - Include all parameters (default)
- <code>none</code> - Include no parameters
- <code>not &lt;param-list&gt;</code> - Include all except the comma separated list of parameter names
- <code>&lt;param-list&gt;</code> - Include all the comma separated list of parameter names

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-params</span><span>=</span><span style="color:#98c379;">"*"</span><span>&gt;Get Some HTML, Including Params&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This div will include all the parameters that a <code>POST</code> would, but they will be URL encoded
and included in the URL, as per usual with a <code>GET</code>.

<h2 id="notes">Notes</h2>- <code>hx-params</code> is inherited and can be placed on a parent element

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-inherit

URL: https://htmx.org/attributes/hx-inherit/

<h1><code>hx-inherit</code></h1>The default behavior for htmx is to “inherit” many attributes automatically: that is, an attribute such as
<a href="https://htmx.org/attributes/hx-target/">hx-target</a> may be placed on a parent element, and all child elements will inherit
that target.  Some people do not like this feature and instead prefer to explicitly specify inheritance for attributes.

To support this mode of development, htmx offers the <code>htmx.config.disableInheritance</code> setting, which can be set to
<code>false</code> to prevent inheritance from being the default behavior for any of the htmx attributes.

The <code>hx-inherit</code> attribute allows you to control the inheritance of attributes manually.

htmx evaluates attribute inheritance as follows:

- when <code>hx-inherit</code> is set on a parent node
<ul>
<li><code>inherit="*"</code> all attribute inheritance for this element will be enabled
- <code>hx-inherit="hx-select hx-get hx-target"</code> enable inheritance for only one or multiple specified attributes


</li>
</ul>Here is an example of a div that shares an <code>hx-target</code> attribute for a set of anchor tags when <code>htmx.config.disableInheritance</code>
is set to false:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#tab-container" </span><span style="color:#d19a66;">hx-inherit</span><span>=</span><span style="color:#98c379;">"hx-target"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">a </span><span style="color:#d19a66;">hx-boost</span><span>=</span><span style="color:#98c379;">"true" </span><span style="color:#d19a66;">href</span><span>=</span><span style="color:#98c379;">"/tab1"</span><span>&gt;Tab 1&lt;/</span><span style="color:#e06c75;">a</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">a </span><span style="color:#d19a66;">hx-boost</span><span>=</span><span style="color:#98c379;">"true" </span><span style="color:#d19a66;">href</span><span>=</span><span style="color:#98c379;">"/tab2"</span><span>&gt;Tab 2&lt;/</span><span style="color:#e06c75;">a</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">a </span><span style="color:#d19a66;">hx-boost</span><span>=</span><span style="color:#98c379;">"true" </span><span style="color:#d19a66;">href</span><span>=</span><span style="color:#98c379;">"/tab3"</span><span>&gt;Tab 3&lt;/</span><span style="color:#e06c75;">a</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h2 id="notes">Notes</h2>- Read more about <a href="https://htmx.org/docs/#inheritance">Attribute Inheritance</a>

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-indicator

URL: https://htmx.org/attributes/hx-indicator/

<h1><code>hx-indicator</code></h1>The <code>hx-indicator</code> attribute allows you to specify the element that will have the <code>htmx-request</code> class
added to it for the duration of the request. This can be used to show spinners or progress indicators
while the request is in flight.

The value of this attribute is a CSS query selector of the element or elements to apply the class to,
or the keyword <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Element/closest"><code>closest</code></a>, followed by a CSS selector,
which will find the closest ancestor element or itself, that matches the given CSS selector (e.g. <code>closest tr</code>);

Here is an example with a spinner adjacent to the button:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-indicator</span><span>=</span><span style="color:#98c379;">"#spinner"</span><span>&gt;
</span><span>        Post It!
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">img  </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"spinner" </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"htmx-indicator" </span><span style="color:#d19a66;">src</span><span>=</span><span style="color:#98c379;">"/img/bars.svg"</span><span>/&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>When a request is in flight, this will cause the <code>htmx-request</code> class to be added to the <code>#spinner</code>
image.  The image also has the <code>htmx-indicator</code> class on it, which defines an opacity transition
that will show the spinner:

<pre data-lang="css" style="background-color:#1f2329;color:#abb2bf;" class="language-css "><code class="language-css" data-lang="css"><span>    </span><span style="color:#d19a66;">.htmx-indicator</span><span>{
</span><span>        opacity:</span><span style="color:#d19a66;">0</span><span>;
</span><span>        transition: opacity </span><span style="color:#d19a66;">500ms </span><span>ease-in;
</span><span>    }
</span><span>    </span><span style="color:#d19a66;">.htmx-request .htmx-indicator</span><span>{
</span><span>        opacity:</span><span style="color:#d19a66;">1</span><span>;
</span><span>    }
</span><span>    </span><span style="color:#d19a66;">.htmx-request.htmx-indicator</span><span>{
</span><span>        opacity:</span><span style="color:#d19a66;">1</span><span>;
</span><span>    }
</span></code></pre>If you would prefer a different effect for showing the spinner you could define and use your own indicator
CSS.  Here is an example that uses <code>display</code> rather than opacity (Note that we use <code>my-indicator</code> instead of <code>htmx-indicator</code>):

<pre data-lang="css" style="background-color:#1f2329;color:#abb2bf;" class="language-css "><code class="language-css" data-lang="css"><span>    </span><span style="color:#d19a66;">.my-indicator</span><span>{
</span><span>        display:none;
</span><span>    }
</span><span>    </span><span style="color:#d19a66;">.htmx-request .my-indicator</span><span>{
</span><span>        display:inline;
</span><span>    }
</span><span>    </span><span style="color:#d19a66;">.htmx-request.my-indicator</span><span>{
</span><span>        display:inline;
</span><span>    }
</span></code></pre>Note that the target of the <code>hx-indicator</code> selector need not be the exact element that you
want to show: it can be any element in the parent hierarchy of the indicator.

Finally, note that the <code>htmx-request</code> class by default is added to the element causing
the request, so you can place an indicator inside of that element and not need to explicitly
call it out with the <code>hx-indicator</code> attribute:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/example"</span><span>&gt;
</span><span>    Post It!
</span><span>   &lt;</span><span style="color:#e06c75;">img  </span><span style="color:#d19a66;">class</span><span>=</span><span style="color:#98c379;">"htmx-indicator" </span><span style="color:#d19a66;">src</span><span>=</span><span style="color:#98c379;">"/img/bars.svg"</span><span>/&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre><h2 id="demo">Demo</h2>This simulates what a spinner might look like in that situation:

<button class="btn" classes="toggle htmx-request:3s">
    Post It!
   <img class="htmx-indicator" src="/img/bars.svg">
</button><h2 id="notes">Notes</h2>- <code>hx-indicator</code> is inherited and can be placed on a parent element
- In the absence of an explicit indicator, the <code>htmx-request</code> class will be added to the element triggering the
request
- If you want to use your own CSS but still use <code>htmx-indicator</code> as class name, then you need to disable <code>includeIndicatorStyles</code>. See <a href="https://htmx.org/docs/#config">Configuring htmx</a>. The easiest way is to add this to the <code>&lt;head&gt;</code> of your HTML:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">meta </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"htmx-config" </span><span style="color:#d19a66;">content</span><span>=</span><span style="color:#98c379;">'{"includeIndicatorStyles": false}'</span><span>&gt;
</span></code></pre><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# htmx.addClass()

URL: https://htmx.org/api/

<h1>Javascript API</h1>While it is not a focus of the library, htmx does provide a small API of helper methods, intended mainly for <a rel="noopener" target="_blank" href="https://extensions.htmx.org">extension development</a> or for working with <a href="https://htmx.org/events/">events</a>.

The <a rel="noopener" target="_blank" href="https://hyperscript.org">hyperscript</a> project is intended to provide more extensive scripting support
for htmx-based applications.

### <a class="zola-anchor" href="#addClass" aria-label="Anchor link for: addClass">#</a>Method - <code>htmx.addClass()</code>This method adds a class to the given element.

<h5 id="parameters"><a class="zola-anchor" href="#parameters" aria-label="Anchor link for: parameters">#</a>Parameters</h5>- <code>elt</code> - the element to add the class to
- <code>class</code> - the class to add

or

- <code>elt</code> - the element to add the class to
- <code>class</code> - the class to add
- <code>delay</code> - delay (in milliseconds ) before class is added

<h5 id="example"><a class="zola-anchor" href="#example" aria-label="Anchor link for: example">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// add the class 'myClass' to the element with the id 'demo'
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">addClass</span><span>(</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">'#demo'</span><span>), </span><span style="color:#98c379;">'myClass'</span><span>);
</span><span>
</span><span>  </span><span style="font-style:italic;color:#848da1;">// add the class 'myClass' to the element with the id 'demo' after 1 second
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">addClass</span><span>(</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">'#demo'</span><span>), </span><span style="color:#98c379;">'myClass'</span><span>, </span><span style="color:#d19a66;">1000</span><span>);
</span></code></pre>### <a class="zola-anchor" href="#ajax" aria-label="Anchor link for: ajax">#</a>Method - <code>htmx.ajax()</code>Issues an htmx-style AJAX request. This method returns a Promise, so a callback can be executed after the content has been inserted into the DOM.

<h5 id="parameters-1"><a class="zola-anchor" href="#parameters-1" aria-label="Anchor link for: parameters-1">#</a>Parameters</h5>- <code>verb</code> - ‘GET’, ‘POST’, etc.
- <code>path</code> - the URL path to make the AJAX
- <code>element</code> - the element to target (defaults to the <code>body</code>)

or

- <code>verb</code> - ‘GET’, ‘POST’, etc.
- <code>path</code> - the URL path to make the AJAX
- <code>selector</code> - a selector for the target

or

- <code>verb</code> - ‘GET’, ‘POST’, etc.
- <code>path</code> - the URL path to make the AJAX
- <code>context</code> - a context object that contains any of the following
<ul>
<li><code>source</code> - the source element of the request, <code>hx-*</code> attrs which affect the request will be resolved against that element and its ancestors
- <code>event</code> - an event that “triggered” the request
- <code>handler</code> - a callback that will handle the response HTML
- <code>target</code> - the target to swap the response into
- <code>swap</code> - how the response will be swapped in relative to the target
- <code>values</code> - values to submit with the request
- <code>headers</code> - headers to submit with the request
- <code>select</code> - allows you to select the content you want swapped from a response


</li>
</ul><h5 id="example-1"><a class="zola-anchor" href="#example-1" aria-label="Anchor link for: example-1">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>    </span><span style="font-style:italic;color:#848da1;">// issue a GET to /example and put the response HTML into #myDiv
</span><span>    </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">ajax</span><span>(</span><span style="color:#98c379;">'GET'</span><span>, </span><span style="color:#98c379;">'/example'</span><span>, </span><span style="color:#98c379;">'#myDiv'</span><span>)
</span><span>
</span><span>    </span><span style="font-style:italic;color:#848da1;">// issue a GET to /example and replace #myDiv with the response
</span><span>    </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">ajax</span><span>(</span><span style="color:#98c379;">'GET'</span><span>, </span><span style="color:#98c379;">'/example'</span><span>, {target:</span><span style="color:#98c379;">'#myDiv'</span><span>, swap:</span><span style="color:#98c379;">'outerHTML'</span><span>})
</span><span>
</span><span>    </span><span style="font-style:italic;color:#848da1;">// execute some code after the content has been inserted into the DOM
</span><span>    </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">ajax</span><span>(</span><span style="color:#98c379;">'GET'</span><span>, </span><span style="color:#98c379;">'/example'</span><span>, </span><span style="color:#98c379;">'#myDiv'</span><span>).</span><span style="color:#56b6c2;">then</span><span>(() </span><span style="color:#c678dd;">=&gt; </span><span>{
</span><span>      </span><span style="font-style:italic;color:#848da1;">// this code will be executed after the 'htmx:afterOnLoad' event,
</span><span>      </span><span style="font-style:italic;color:#848da1;">// and before the 'htmx:xhr:loadend' event
</span><span>      </span><span style="color:#e5c07b;">console</span><span>.</span><span style="color:#56b6c2;">log</span><span>(</span><span style="color:#98c379;">'Content inserted successfully!'</span><span>);
</span><span>    });
</span><span>
</span></code></pre>### <a class="zola-anchor" href="#closest" aria-label="Anchor link for: closest">#</a>Method - <code>htmx.closest()</code>Finds the closest matching element in the given elements parentage, inclusive of the element

<h5 id="parameters-2"><a class="zola-anchor" href="#parameters-2" aria-label="Anchor link for: parameters-2">#</a>Parameters</h5>- <code>elt</code> - the element to find the selector from
- <code>selector</code> - the selector to find

<h5 id="example-2"><a class="zola-anchor" href="#example-2" aria-label="Anchor link for: example-2">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// find the closest enclosing div of the element with the id 'demo'
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">closest</span><span>(</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">'#demo'</span><span>), </span><span style="color:#98c379;">'div'</span><span>);
</span></code></pre>### <a class="zola-anchor" href="#config" aria-label="Anchor link for: config">#</a>Property - <code>htmx.config</code>A property holding the configuration htmx uses at runtime.

Note that using a <a href="https://htmx.org/docs/#config">meta tag</a> is the preferred mechanism for setting these properties.

<h5 id="properties"><a class="zola-anchor" href="#properties" aria-label="Anchor link for: properties">#</a>Properties</h5>- <code>attributesToSettle:["class", "style", "width", "height"]</code> - array of strings: the attributes to settle during the settling phase
- <code>refreshOnHistoryMiss:false</code> - boolean: if set to <code>true</code> htmx will issue a full page refresh on history misses rather than use an AJAX request
- <code>defaultSettleDelay:20</code> - int: the default delay between completing the content swap and settling attributes
- <code>defaultSwapDelay:0</code> - int: the default delay between receiving a response from the server and doing the swap
- <code>defaultSwapStyle:'innerHTML'</code> - string: the default swap style to use if <a href="https://htmx.org/attributes/hx-swap/"><code>hx-swap</code></a> is omitted
- <code>historyCacheSize:10</code> - int: the number of pages to keep in <code>localStorage</code> for history support
- <code>historyEnabled:true</code> - boolean: whether or not to use history
- <code>includeIndicatorStyles:true</code> - boolean: if true, htmx will inject a small amount of CSS into the page to make indicators invisible unless the <code>htmx-indicator</code> class is present
- <code>indicatorClass:'htmx-indicator'</code> - string: the class to place on indicators when a request is in flight
- <code>requestClass:'htmx-request'</code> - string: the class to place on triggering elements when a request is in flight
- <code>addedClass:'htmx-added'</code> - string: the class to temporarily place on elements that htmx has added to the DOM
- <code>settlingClass:'htmx-settling'</code> - string: the class to place on target elements when htmx is in the settling phase
- <code>swappingClass:'htmx-swapping'</code> - string: the class to place on target elements when htmx is in the swapping phase
- <code>allowEval:true</code> - boolean: allows the use of eval-like functionality in htmx, to enable <code>hx-vars</code>, trigger conditions &amp; script tag evaluation.  Can be set to <code>false</code> for CSP compatibility.
- <code>allowScriptTags:true</code> - boolean: allows script tags to be evaluated in new content
- <code>inlineScriptNonce:''</code> - string: the <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/HTML/Global_attributes/nonce">nonce</a> to add to inline scripts
- <code>inlineStyleNonce:''</code> - string: the <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/HTML/Global_attributes/nonce">nonce</a> to add to inline styles
- <code>withCredentials:false</code> - boolean: allow cross-site Access-Control requests using credentials such as cookies, authorization headers or TLS client certificates
- <code>timeout:0</code> - int: the number of milliseconds a request can take before automatically being terminated
- <code>wsReconnectDelay:'full-jitter'</code> - string/function: the default implementation of <code>getWebSocketReconnectDelay</code> for reconnecting after unexpected connection loss by the event code <code>Abnormal Closure</code>, <code>Service Restart</code> or <code>Try Again Later</code>
- <code>wsBinaryType:'blob'</code> - string: the <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/WebSocket/binaryType">the type of binary data</a> being received over the WebSocket connection
- <code>disableSelector:"[hx-disable], [data-hx-disable]"</code> - array of strings: htmx will not process elements with this attribute on it or a parent
- <code>scrollBehavior:'smooth'</code> - string: the behavior for a boosted link on page transitions. The allowed values are <code>auto</code> and <code>smooth</code>. Smooth will smoothscroll to the top of the page while auto will behave like a vanilla link.
- <code>defaultFocusScroll:false</code> - boolean: if the focused element should be scrolled into view, can be overridden using the <a href="https://htmx.org/attributes/hx-swap/#focus-scroll">focus-scroll</a> swap modifier
- <code>getCacheBusterParam:false</code> - boolean: if set to true htmx will append the target element to the <code>GET</code> request in the format <code>org.htmx.cache-buster=targetElementId</code>
- <code>globalViewTransitions:false</code> - boolean: if set to <code>true</code>, htmx will use the <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API">View Transition</a> API when swapping in new content.
- <code>methodsThatUseUrlParams:["get"]</code> - array of strings: htmx will format requests with these methods by encoding their parameters in the URL, not the request body
- <code>selfRequestsOnly:true</code> - boolean: whether to only allow AJAX requests to the same domain as the current document
- <code>ignoreTitle:false</code> - boolean: if set to <code>true</code> htmx will not update the title of the document when a <code>title</code> tag is found in new content
- <code>scrollIntoViewOnBoost:true</code> - boolean: whether or not the target of a boosted element is scrolled into the viewport. If <code>hx-target</code> is omitted on a boosted element, the target defaults to <code>body</code>, causing the page to scroll to the top.
- <code>triggerSpecsCache:null</code> - object: the cache to store evaluated trigger specifications into, improving parsing performance at the cost of more memory usage. You may define a simple object to use a never-clearing cache, or implement your own system using a <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Proxy">proxy object</a> |

<h5 id="example-3"><a class="zola-anchor" href="#example-3" aria-label="Anchor link for: example-3">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// update the history cache size to 30
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#e06c75;">config</span><span>.</span><span style="color:#e06c75;">historyCacheSize </span><span>= </span><span style="color:#d19a66;">30</span><span>;
</span></code></pre>### <a class="zola-anchor" href="#createEventSource" aria-label="Anchor link for: createEventSource">#</a>Property - <code>htmx.createEventSource</code>A property used to create new <a rel="noopener" target="_blank" href="https://github.com/bigskysoftware/htmx-extensions/blob/main/src/sse/README.md">Server Sent Event</a> sources.  This can be updated
to provide custom SSE setup.

<h5 id="value"><a class="zola-anchor" href="#value" aria-label="Anchor link for: value">#</a>Value</h5>- <code>func(url)</code> - a function that takes a URL string and returns a new <code>EventSource</code>

<h5 id="example-4"><a class="zola-anchor" href="#example-4" aria-label="Anchor link for: example-4">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// override SSE event sources to not use credentials
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">createEventSource </span><span>= </span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">url</span><span>) {
</span><span>    </span><span style="color:#c678dd;">return </span><span>new EventSource(</span><span style="color:#e06c75;">url</span><span>, {withCredentials:</span><span style="color:#d19a66;">false</span><span>});
</span><span>  };
</span></code></pre>### <a class="zola-anchor" href="#createWebSocket" aria-label="Anchor link for: createWebSocket">#</a>Property - <code>htmx.createWebSocket</code>A property used to create new <a rel="noopener" target="_blank" href="https://github.com/bigskysoftware/htmx-extensions/blob/main/src/ws/README.md">WebSocket</a>.  This can be updated
to provide custom WebSocket setup.

<h5 id="value-1"><a class="zola-anchor" href="#value-1" aria-label="Anchor link for: value-1">#</a>Value</h5>- <code>func(url)</code> - a function that takes a URL string and returns a new <code>WebSocket</code>

<h5 id="example-5"><a class="zola-anchor" href="#example-5" aria-label="Anchor link for: example-5">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// override WebSocket to use a specific protocol
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">createWebSocket </span><span>= </span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">url</span><span>) {
</span><span>    </span><span style="color:#c678dd;">return </span><span>new WebSocket(</span><span style="color:#e06c75;">url</span><span>, [</span><span style="color:#98c379;">'wss'</span><span>]);
</span><span>  };
</span></code></pre>### <a class="zola-anchor" href="#defineExtension" aria-label="Anchor link for: defineExtension">#</a>Method - <code>htmx.defineExtension()</code>Defines a new htmx <a rel="noopener" target="_blank" href="https://extensions.htmx.org">extension</a>.

<h5 id="parameters-3"><a class="zola-anchor" href="#parameters-3" aria-label="Anchor link for: parameters-3">#</a>Parameters</h5>- <code>name</code> - the extension name
- <code>ext</code> - the extension definition

<h5 id="example-6"><a class="zola-anchor" href="#example-6" aria-label="Anchor link for: example-6">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// defines a silly extension that just logs the name of all events triggered
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">defineExtension</span><span>(</span><span style="color:#98c379;">"silly"</span><span>, {
</span><span>    </span><span style="color:#61afef;">onEvent </span><span>: </span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">name</span><span>, </span><span style="color:#e06c75;">evt</span><span>) {
</span><span>      </span><span style="color:#e5c07b;">console</span><span>.</span><span style="color:#56b6c2;">log</span><span>(</span><span style="color:#98c379;">"Event " </span><span>+ </span><span style="color:#e06c75;">name </span><span>+ </span><span style="color:#98c379;">" was triggered!"</span><span>)
</span><span>    }
</span><span>  });
</span></code></pre>### <a class="zola-anchor" href="#find" aria-label="Anchor link for: find">#</a>Method - <code>htmx.find()</code>Finds an element matching the selector

<h5 id="parameters-4"><a class="zola-anchor" href="#parameters-4" aria-label="Anchor link for: parameters-4">#</a>Parameters</h5>- <code>selector</code> - the selector to match

or

- <code>elt</code> - the root element to find the matching element in, inclusive
- <code>selector</code> - the selector to match

<h5 id="example-7"><a class="zola-anchor" href="#example-7" aria-label="Anchor link for: example-7">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>    </span><span style="font-style:italic;color:#848da1;">// find div with id my-div
</span><span>    </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">div </span><span>= </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">"#my-div"</span><span>)
</span><span>
</span><span>    </span><span style="font-style:italic;color:#848da1;">// find div with id another-div within that div
</span><span>    </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">anotherDiv </span><span>= </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#e06c75;">div</span><span>, </span><span style="color:#98c379;">"#another-div"</span><span>)
</span></code></pre>### <a class="zola-anchor" href="#findAll" aria-label="Anchor link for: findAll">#</a>Method - <code>htmx.findAll()</code>Finds all elements matching the selector

<h5 id="parameters-5"><a class="zola-anchor" href="#parameters-5" aria-label="Anchor link for: parameters-5">#</a>Parameters</h5>- <code>selector</code> - the selector to match

or

- <code>elt</code> - the root element to find the matching elements in, inclusive
- <code>selector</code> - the selector to match

<h5 id="example-8"><a class="zola-anchor" href="#example-8" aria-label="Anchor link for: example-8">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>    </span><span style="font-style:italic;color:#848da1;">// find all divs
</span><span>    </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">allDivs </span><span>= </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">findAll</span><span>(</span><span style="color:#98c379;">"div"</span><span>)
</span><span>
</span><span>    </span><span style="font-style:italic;color:#848da1;">// find all paragraphs within a given div
</span><span>    </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">allParagraphsInMyDiv </span><span>= </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">findAll</span><span>(</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">"#my-div"</span><span>), </span><span style="color:#98c379;">"p"</span><span>)
</span></code></pre>### <a class="zola-anchor" href="#logAll" aria-label="Anchor link for: logAll">#</a>Method - <code>htmx.logAll()</code>Log all htmx events, useful for debugging.

<h5 id="example-9"><a class="zola-anchor" href="#example-9" aria-label="Anchor link for: example-9">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>    </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">logAll</span><span>();
</span></code></pre>### <a class="zola-anchor" href="#logNone" aria-label="Anchor link for: logNone">#</a>Method - <code>htmx.logNone()</code>Log no htmx events, call this to turn off the debugger if you previously enabled it.

<h5 id="example-10"><a class="zola-anchor" href="#example-10" aria-label="Anchor link for: example-10">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>    </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">logNone</span><span>();
</span></code></pre>### <a class="zola-anchor" href="#logger" aria-label="Anchor link for: logger">#</a>Property - <code>htmx.logger</code>The logger htmx uses to log with

<h5 id="value-2"><a class="zola-anchor" href="#value-2" aria-label="Anchor link for: value-2">#</a>Value</h5>- <code>func(elt, eventName, detail)</code> - a function that takes an element, eventName and event detail and logs it

<h5 id="example-11"><a class="zola-anchor" href="#example-11" aria-label="Anchor link for: example-11">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>    </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">logger </span><span>= </span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">elt</span><span>, </span><span style="color:#e06c75;">event</span><span>, </span><span style="color:#e06c75;">data</span><span>) {
</span><span>        </span><span style="color:#c678dd;">if</span><span>(</span><span style="color:#e5c07b;">console</span><span>) {
</span><span>            </span><span style="color:#e5c07b;">console</span><span>.</span><span style="color:#56b6c2;">log</span><span>(</span><span style="color:#98c379;">"INFO:"</span><span>, event, </span><span style="color:#e06c75;">elt</span><span>, </span><span style="color:#e06c75;">data</span><span>);
</span><span>        }
</span><span>    }
</span></code></pre>### <a class="zola-anchor" href="#off" aria-label="Anchor link for: off">#</a>Method - <code>htmx.off()</code>Removes an event listener from an element

<h5 id="parameters-6"><a class="zola-anchor" href="#parameters-6" aria-label="Anchor link for: parameters-6">#</a>Parameters</h5>- <code>eventName</code> - the event name to remove the listener from
- <code>listener</code> - the listener to remove

or

- <code>target</code> - the element to remove the listener from
- <code>eventName</code> - the event name to remove the listener from
- <code>listener</code> - the listener to remove

<h5 id="example-12"><a class="zola-anchor" href="#example-12" aria-label="Anchor link for: example-12">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>    </span><span style="font-style:italic;color:#848da1;">// remove this click listener from the body
</span><span>    </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">off</span><span>(</span><span style="color:#98c379;">"click"</span><span>, </span><span style="color:#e06c75;">myEventListener</span><span>);
</span><span>
</span><span>    </span><span style="font-style:italic;color:#848da1;">// remove this click listener from the given div
</span><span>    </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">off</span><span>(</span><span style="color:#98c379;">"#my-div"</span><span>, </span><span style="color:#98c379;">"click"</span><span>, </span><span style="color:#e06c75;">myEventListener</span><span>)
</span></code></pre>### <a class="zola-anchor" href="#on" aria-label="Anchor link for: on">#</a>Method - <code>htmx.on()</code>Adds an event listener to an element

<h5 id="parameters-7"><a class="zola-anchor" href="#parameters-7" aria-label="Anchor link for: parameters-7">#</a>Parameters</h5>- <code>eventName</code> - the event name to add the listener for
- <code>listener</code> - the listener to add

or

- <code>target</code> - the element to add the listener to
- <code>eventName</code> - the event name to add the listener for
- <code>listener</code> - the listener to add

<h5 id="example-13"><a class="zola-anchor" href="#example-13" aria-label="Anchor link for: example-13">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>    </span><span style="font-style:italic;color:#848da1;">// add a click listener to the body
</span><span>    </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">myEventListener </span><span>= </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">on</span><span>(</span><span style="color:#98c379;">"click"</span><span>, </span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">evt</span><span>){ </span><span style="color:#e5c07b;">console</span><span>.</span><span style="color:#56b6c2;">log</span><span>(</span><span style="color:#e06c75;">evt</span><span>); });
</span><span>
</span><span>    </span><span style="font-style:italic;color:#848da1;">// add a click listener to the given div
</span><span>    </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">myEventListener </span><span>= </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">on</span><span>(</span><span style="color:#98c379;">"#my-div"</span><span>, </span><span style="color:#98c379;">"click"</span><span>, </span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">evt</span><span>){ </span><span style="color:#e5c07b;">console</span><span>.</span><span style="color:#56b6c2;">log</span><span>(</span><span style="color:#e06c75;">evt</span><span>); });
</span></code></pre>### <a class="zola-anchor" href="#onLoad" aria-label="Anchor link for: onLoad">#</a>Method - <code>htmx.onLoad()</code>Adds a callback for the <code>htmx:load</code> event. This can be used to process new content, for example
initializing the content with a javascript library

<h5 id="parameters-8"><a class="zola-anchor" href="#parameters-8" aria-label="Anchor link for: parameters-8">#</a>Parameters</h5>- <code>callback(elt)</code> - the callback to call on newly loaded content

<h5 id="example-14"><a class="zola-anchor" href="#example-14" aria-label="Anchor link for: example-14">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>    </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">onLoad</span><span>(</span><span style="color:#c678dd;">function</span><span>(</span><span style="color:#e06c75;">elt</span><span>){
</span><span>        </span><span style="color:#e06c75;">MyLibrary</span><span>.</span><span style="color:#61afef;">init</span><span>(</span><span style="color:#e06c75;">elt</span><span>);
</span><span>    })
</span></code></pre>### <a class="zola-anchor" href="#parseInterval" aria-label="Anchor link for: parseInterval">#</a>Method - <code>htmx.parseInterval()</code>Parses an interval string consistent with the way htmx does.  Useful for plugins that have timing-related attributes.

Caution: Accepts an int followed by either <code>s</code> or <code>ms</code>. All other values use <code>parseFloat</code>

<h5 id="parameters-9"><a class="zola-anchor" href="#parameters-9" aria-label="Anchor link for: parameters-9">#</a>Parameters</h5>- <code>str</code> - timing string

<h5 id="example-15"><a class="zola-anchor" href="#example-15" aria-label="Anchor link for: example-15">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>    </span><span style="font-style:italic;color:#848da1;">// returns 3000
</span><span>    </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">milliseconds </span><span>= </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">parseInterval</span><span>(</span><span style="color:#98c379;">"3s"</span><span>);
</span><span>
</span><span>    </span><span style="font-style:italic;color:#848da1;">// returns 3 - Caution
</span><span>    </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">milliseconds </span><span>= </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">parseInterval</span><span>(</span><span style="color:#98c379;">"3m"</span><span>);
</span></code></pre>### <a class="zola-anchor" href="#process" aria-label="Anchor link for: process">#</a>Method - <code>htmx.process()</code>Processes new content, enabling htmx behavior.  This can be useful if you have content that is added to the DOM
outside of the normal htmx request cycle but still want htmx attributes to work.

<h5 id="parameters-10"><a class="zola-anchor" href="#parameters-10" aria-label="Anchor link for: parameters-10">#</a>Parameters</h5>- <code>elt</code> - element to process

<h5 id="example-16"><a class="zola-anchor" href="#example-16" aria-label="Anchor link for: example-16">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  document.body.</span><span style="color:#e06c75;">innerHTML </span><span>= </span><span style="color:#98c379;">"&lt;div hx-get='/example'&gt;Get it!&lt;/div&gt;"
</span><span>  </span><span style="font-style:italic;color:#848da1;">// process the newly added content
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">process</span><span>(document.body);
</span></code></pre>### <a class="zola-anchor" href="#remove" aria-label="Anchor link for: remove">#</a>Method - <code>htmx.remove()</code>Removes an element from the DOM

<h5 id="parameters-11"><a class="zola-anchor" href="#parameters-11" aria-label="Anchor link for: parameters-11">#</a>Parameters</h5>- <code>elt</code> - element to remove

or

- <code>elt</code> - element to remove
- <code>delay</code> - delay (in milliseconds ) before element is removed

<h5 id="example-17"><a class="zola-anchor" href="#example-17" aria-label="Anchor link for: example-17">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// removes my-div from the DOM
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">remove</span><span>(</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">"#my-div"</span><span>));
</span><span>
</span><span>  </span><span style="font-style:italic;color:#848da1;">// removes my-div from the DOM after a delay of 2 seconds
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">remove</span><span>(</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">"#my-div"</span><span>), </span><span style="color:#d19a66;">2000</span><span>);
</span></code></pre>### <a class="zola-anchor" href="#removeClass" aria-label="Anchor link for: removeClass">#</a>Method - <code>htmx.removeClass()</code>Removes a class from the given element

<h5 id="parameters-12"><a class="zola-anchor" href="#parameters-12" aria-label="Anchor link for: parameters-12">#</a>Parameters</h5>- <code>elt</code> - element to remove the class from
- <code>class</code> - the class to remove

or

- <code>elt</code> - element to remove the class from
- <code>class</code> - the class to remove
- <code>delay</code> - delay (in milliseconds ) before class is removed

<h5 id="example-18"><a class="zola-anchor" href="#example-18" aria-label="Anchor link for: example-18">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// removes .myClass from my-div
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">removeClass</span><span>(</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">"#my-div"</span><span>), </span><span style="color:#98c379;">"myClass"</span><span>);
</span><span>
</span><span>  </span><span style="font-style:italic;color:#848da1;">// removes .myClass from my-div after 6 seconds
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">removeClass</span><span>(</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">"#my-div"</span><span>), </span><span style="color:#98c379;">"myClass"</span><span>, </span><span style="color:#d19a66;">6000</span><span>);
</span></code></pre>### <a class="zola-anchor" href="#removeExtension" aria-label="Anchor link for: removeExtension">#</a>Method - <code>htmx.removeExtension()</code>Removes the given extension from htmx

<h5 id="parameters-13"><a class="zola-anchor" href="#parameters-13" aria-label="Anchor link for: parameters-13">#</a>Parameters</h5>- <code>name</code> - the name of the extension to remove

<h5 id="example-19"><a class="zola-anchor" href="#example-19" aria-label="Anchor link for: example-19">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">removeExtension</span><span>(</span><span style="color:#98c379;">"my-extension"</span><span>);
</span></code></pre>### <a class="zola-anchor" href="#swap" aria-label="Anchor link for: swap">#</a>Method - <code>htmx.swap()</code>Performs swapping (and settling) of HTML content

<h5 id="parameters-14"><a class="zola-anchor" href="#parameters-14" aria-label="Anchor link for: parameters-14">#</a>Parameters</h5>- <code>target</code> - the HTML element or string selector of swap target
- <code>content</code> - string representation of content to be swapped
- <code>swapSpec</code> - swapping specification, representing parameters from <code>hx-swap</code>
<ul>
<li><code>swapStyle</code> (required) - swapping style (<code>innerHTML</code>, <code>outerHTML</code>, <code>beforebegin</code> etc)
- <code>swapDelay</code>, <code>settleDelay</code> (number) - delays before swapping and settling respectively
- <code>transition</code> (bool) - whether to use HTML transitions for swap
- <code>ignoreTitle</code> (bool) - disables page title updates
- <code>head</code> (string) - specifies <code>head</code> tag handling strategy (<code>merge</code> or <code>append</code>). Leave empty to disable head handling
- <code>scroll</code>, <code>scrollTarget</code>, <code>show</code>, <code>showTarget</code>, <code>focusScroll</code> - specifies scroll handling after swap


</li>
<li><code>swapOptions</code> - additional <em>optional</em> parameters for swapping
- <code>select</code> - selector for the content to be swapped (equivalent of <code>hx-select</code>)
- <code>selectOOB</code> - selector for the content to be swapped out-of-band (equivalent of <code>hx-select-oob</code>)
- <code>eventInfo</code> - an object to be attached to <code>htmx:afterSwap</code> and <code>htmx:afterSettle</code> elements
- <code>anchor</code> - an anchor element that triggered scroll, will be scrolled into view on settle. Provides simple alternative to full scroll handling
- <code>contextElement</code> - DOM element that serves as context to swapping operation. Currently used to find extensions enabled for specific element
- <code>afterSwapCallback</code>, <code>afterSettleCallback</code> - callback functions called after swap and settle respectively. Take no arguments


</li>
</ul><h5 id="example-20"><a class="zola-anchor" href="#example-20" aria-label="Anchor link for: example-20">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>    </span><span style="font-style:italic;color:#848da1;">// swap #output element inner HTML with div element with "Swapped!" text
</span><span>    </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">swap</span><span>(</span><span style="color:#98c379;">"#output"</span><span>, </span><span style="color:#98c379;">"&lt;div&gt;Swapped!&lt;/div&gt;"</span><span>, {swapStyle: </span><span style="color:#98c379;">'innerHTML'</span><span>});
</span></code></pre>### <a class="zola-anchor" href="#takeClass" aria-label="Anchor link for: takeClass">#</a>Method - <code>htmx.takeClass()</code>Takes the given class from its siblings, so that among its siblings, only the given element will have the class.

<h5 id="parameters-15"><a class="zola-anchor" href="#parameters-15" aria-label="Anchor link for: parameters-15">#</a>Parameters</h5>- <code>elt</code> - the element that will take the class
- <code>class</code> - the class to take

<h5 id="example-21"><a class="zola-anchor" href="#example-21" aria-label="Anchor link for: example-21">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// takes the selected class from tab2's siblings
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">takeClass</span><span>(</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">"#tab2"</span><span>), </span><span style="color:#98c379;">"selected"</span><span>);
</span></code></pre>### <a class="zola-anchor" href="#toggleClass" aria-label="Anchor link for: toggleClass">#</a>Method - <code>htmx.toggleClass()</code>Toggles the given class on an element

<h5 id="parameters-16"><a class="zola-anchor" href="#parameters-16" aria-label="Anchor link for: parameters-16">#</a>Parameters</h5>- <code>elt</code> - the element to toggle the class on
- <code>class</code> - the class to toggle

<h5 id="example-22"><a class="zola-anchor" href="#example-22" aria-label="Anchor link for: example-22">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// toggles the selected class on tab2
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">toggleClass</span><span>(</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">"#tab2"</span><span>), </span><span style="color:#98c379;">"selected"</span><span>);
</span></code></pre>### <a class="zola-anchor" href="#trigger" aria-label="Anchor link for: trigger">#</a>Method - <code>htmx.trigger()</code>Triggers a given event on an element

<h5 id="parameters-17"><a class="zola-anchor" href="#parameters-17" aria-label="Anchor link for: parameters-17">#</a>Parameters</h5>- <code>elt</code> - the element to trigger the event on
- <code>name</code> - the name of the event to trigger
- <code>detail</code> - details for the event

<h5 id="example-23"><a class="zola-anchor" href="#example-23" aria-label="Anchor link for: example-23">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// triggers the myEvent event on #tab2 with the answer 42
</span><span>  </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#61afef;">trigger</span><span>(</span><span style="color:#98c379;">"#tab2"</span><span>, </span><span style="color:#98c379;">"myEvent"</span><span>, {answer:</span><span style="color:#d19a66;">42</span><span>});
</span></code></pre>### <a class="zola-anchor" href="#values" aria-label="Anchor link for: values">#</a>Method - <code>htmx.values()</code>Returns the input values that would resolve for a given element via the htmx value resolution mechanism

<h5 id="parameters-18"><a class="zola-anchor" href="#parameters-18" aria-label="Anchor link for: parameters-18">#</a>Parameters</h5>- <code>elt</code> - the element to resolve values on
- <code>request type</code> - the request type (e.g. <code>get</code> or <code>post</code>)  non-GET’s will include the enclosing form of the element.
Defaults to <code>post</code>

<h5 id="example-24"><a class="zola-anchor" href="#example-24" aria-label="Anchor link for: example-24">#</a>Example</h5><pre data-lang="js" style="background-color:#1f2329;color:#abb2bf;" class="language-js "><code class="language-js" data-lang="js"><span>  </span><span style="font-style:italic;color:#848da1;">// gets the values associated with this form
</span><span>  </span><span style="color:#c678dd;">var </span><span style="color:#e06c75;">values </span><span>= </span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">values</span><span>(</span><span style="color:#e06c75;">htmx</span><span>.</span><span style="color:#56b6c2;">find</span><span>(</span><span style="color:#98c379;">"#myForm"</span><span>));
</span></code></pre><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-patch

URL: https://htmx.org/attributes/hx-patch/

<h1><code>hx-patch</code></h1>The <code>hx-patch</code> attribute will cause an element to issue a <code>PATCH</code> to the specified URL and swap
the HTML into the DOM using a swap strategy:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-patch</span><span>=</span><span style="color:#98c379;">"/account" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"body"</span><span>&gt;
</span><span>  Patch Your Account
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>This example will cause the <code>button</code> to issue a <code>PATCH</code> to <code>/account</code> and swap the returned HTML into
the <code>innerHTML</code> of the <code>body</code>.

<h2 id="notes">Notes</h2>- <code>hx-patch</code> is not inherited
- You can control the target of the swap using the <a href="https://htmx.org/attributes/hx-target/">hx-target</a> attribute
- You can control the swap strategy by using the <a href="https://htmx.org/attributes/hx-swap/">hx-swap</a> attribute
- You can control what event triggers the request with the <a href="https://htmx.org/attributes/hx-trigger/">hx-trigger</a> attribute
- You can control the data submitted with the request in various ways, documented here: <a href="https://htmx.org/docs/#parameters">Parameters</a>

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-include

URL: https://htmx.org/attributes/hx-include/

<h1><code>hx-include</code></h1>The <code>hx-include</code> attribute allows you to include additional element values in an AJAX request. The value of this
attribute can be:

- A CSS query selector of the elements to include.
- <code>this</code> which will include the descendants of the element.
- <code>closest &lt;CSS selector&gt;</code> which will find the <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Element/closest">closest</a>
ancestor element or itself, that matches the given CSS selector
(e.g. <code>closest tr</code> will target the closest table row to the element).
- <code>find &lt;CSS selector&gt;</code> which will find the first child descendant element that matches the given CSS selector.
- <code>next &lt;CSS selector&gt;</code> which will scan the DOM forward for the first element that matches the given CSS selector.
(e.g. <code>next .error</code> will target the closest following sibling element with <code>error</code> class)
- <code>previous &lt;CSS selector&gt;</code> which will scan the DOM backwards for the first element that matches the given CSS selector.
(e.g <code>previous .error</code> will target the closest previous sibling with <code>error</code> class)

Here is an example that includes a separate input value:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/register" </span><span style="color:#d19a66;">hx-include</span><span>=</span><span style="color:#98c379;">"[name='email']"</span><span>&gt;
</span><span>        Register!
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>    Enter email: &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"email"</span><span>/&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This is a little contrived as you would typically enclose both of these elements in a <code>form</code> and submit
the value automatically, but it demonstrates the concept.

Note that if you include a non-input element, all input elements enclosed in that element will be included.

<h2 id="notes">Notes</h2>- <code>hx-include</code> is inherited and can be placed on a parent element
- While <code>hx-include</code> is inherited, it is evaluated from the element triggering the request. It is easy to get confused
when working with the extended selectors such as <code>find</code> and <code>closest</code>.<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-include</span><span>=</span><span style="color:#98c379;">"find input"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/register"</span><span>&gt;
</span><span>        Register!
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>    Enter email: &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"email"</span><span>/&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>
In the above example, when clicking on the button, the <code>find input</code> selector is resolved from the button itself, which
does not return any element here, since the button doesn’t have any <code>input</code> child, thus in this case, raises an error.
- A standard CSS selector resolves
to <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Document/querySelectorAll">document.querySelectorAll</a> and will include
multiple elements, while the extended selectors such as <code>find</code> or <code>next</code> only return a single element at most to
include

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-history

URL: https://htmx.org/attributes/hx-history/

<h1><code>hx-history</code></h1>Set the <code>hx-history</code> attribute to <code>false</code> on any element in the current document, or any html fragment loaded into the current document by htmx, to prevent sensitive data being saved to the localStorage cache when htmx takes a snapshot of the page state.

History navigation will work as expected, but on restoration the URL will be requested from the server instead of the history cache.

Here is an example:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">html</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">body</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-history</span><span>=</span><span style="color:#98c379;">"false"</span><span>&gt;
</span><span> ...
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">body</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">html</span><span>&gt;
</span></code></pre><h2 id="notes">Notes</h2>- <code>hx-history="false"</code> can be present <em>anywhere</em> in the document to embargo the current page state from the history cache (i.e. even outside the element specified for the history snapshot <a href="https://htmx.org/attributes/hx-history-elt/">hx-history-elt</a>).

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-history-elt

URL: https://htmx.org/attributes/hx-history-elt/

<h1><code>hx-history-elt</code></h1>The <code>hx-history-elt</code> attribute allows you to specify the element that will be used to snapshot and
restore page state during navigation.  By default, the <code>body</code> tag is used.  This is typically
good enough for most setups, but you may want to narrow it down to a child element.  Just make
sure that the element is always visible in your application, or htmx will not be able to restore
history navigation properly.

Here is an example:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">html</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">body</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"content" </span><span style="color:#d19a66;">hx-history-elt</span><span>&gt;
</span><span> ...
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">body</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">html</span><span>&gt;
</span></code></pre><h2 id="notes">Notes</h2>- <code>hx-history-elt</code> is not inherited
- In most cases we don’t recommend narrowing the history snapshot

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-headers

URL: https://htmx.org/attributes/hx-headers/

<h1><code>hx-headers</code></h1>The <code>hx-headers</code> attribute allows you to add to the headers that will be submitted with an AJAX request.

By default, the value of this attribute is a list of name-expression values in <a rel="noopener" target="_blank" href="https://www.json.org/json-en.html">JSON (JavaScript Object Notation)</a>
format.

If you wish for <code>hx-headers</code> to <em>evaluate</em> the values given, you can prefix the values with <code>javascript:</code> or <code>js:</code>.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-headers</span><span>=</span><span style="color:#98c379;">'{"myHeader": "My Value"}'</span><span>&gt;Get Some HTML, Including A Custom Header in the Request&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h2 id="security-considerations">Security Considerations</h2>- By default, the value of <code>hx-headers</code> must be valid <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Glossary/JSON">JSON</a>.
It is <strong>not</strong> dynamically computed.  If you use the <code>javascript:</code> prefix, be aware that you are introducing
security considerations, especially when dealing with user input such as query strings or user-generated content,
which could introduce a <a rel="noopener" target="_blank" href="https://owasp.org/www-community/attacks/xss/">Cross-Site Scripting (XSS)</a> vulnerability.

<h2 id="notes">Notes</h2>- <code>hx-headers</code> is inherited and can be placed on a parent element.
- A child declaration of a header overrides a parent declaration.

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-ext

URL: https://htmx.org/attributes/hx-ext/

<h1><code>hx-ext</code></h1>The <code>hx-ext</code> attribute enables an htmx <a rel="noopener" target="_blank" href="https://extensions.htmx.org">extension</a> for an element and all its children.

The value can be a single extension name or a comma separated list of extensions to apply.

The <code>hx-ext</code> tag may be placed on parent elements if you want a plugin to apply to an entire swath of the DOM,
and on the <code>body</code> tag for it to apply to all htmx requests.

<h2 id="notes">Notes</h2>- <code>hx-ext</code> is both inherited and merged with parent elements, so you can specify extensions on any element in the DOM
hierarchy and it will apply to all child elements.
- You can ignore an extension that is defined by a parent node using <code>hx-ext="ignore:extensionName"</code>

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-ext</span><span>=</span><span style="color:#98c379;">"example"</span><span>&gt;
</span><span>  "Example" extension is used in this part of the tree...
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-ext</span><span>=</span><span style="color:#98c379;">"ignore:example"</span><span>&gt;
</span><span>    ... but it will not be used in this part.
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-encoding

URL: https://htmx.org/attributes/hx-encoding/

<h1><code>hx-encoding</code></h1>The <code>hx-encoding</code> attribute allows you to switch the request encoding from the usual <code>application/x-www-form-urlencoded</code>
encoding to <code>multipart/form-data</code>, usually to support file uploads in an ajax request.

The value of this attribute should be <code>multipart/form-data</code>.

The <code>hx-encoding</code> tag may be placed on parent elements.

<h2 id="notes">Notes</h2>- <code>hx-encoding</code> is inherited and can be placed on a parent element

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-disable

URL: https://htmx.org/attributes/hx-disable/

<h1><code>hx-disable</code></h1>The <code>hx-disable</code> attribute will disable htmx processing for a given element and all its children.  This can be
useful as a backup for HTML escaping, when you include user generated content in your site, and you want to
prevent malicious scripting attacks.

The value of the tag is ignored, and it cannot be reversed by any content beneath it.

<h2 id="notes">Notes</h2>- <code>hx-disable</code> is inherited

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-disinherit

URL: https://htmx.org/attributes/hx-disinherit/

<h1><code>hx-disinherit</code></h1>The default behavior for htmx is to “inherit” many attributes automatically: that is, an attribute such as
<a href="https://htmx.org/attributes/hx-target/">hx-target</a> may be placed on a parent element, and all child elements will inherit
that target.

The <code>hx-disinherit</code> attribute allows you to control this automatic attribute inheritance. An example scenario is to
allow you to place an <code>hx-boost</code> on the <code>body</code> element of a page, but overriding that behavior in a specific part
of the page to allow for more specific behaviors.

htmx evaluates attribute inheritance as follows:

- when <code>hx-disinherit</code> is set on a parent node
<ul>
<li><code>hx-disinherit="*"</code> all attribute inheritance for this element will be disabled
- <code>hx-disinherit="hx-select hx-get hx-target"</code> disable inheritance for only one or multiple specified attributes


</li>
</ul><pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-boost</span><span>=</span><span style="color:#98c379;">"true" </span><span style="color:#d19a66;">hx-select</span><span>=</span><span style="color:#98c379;">"#content" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#content" </span><span style="color:#d19a66;">hx-disinherit</span><span>=</span><span style="color:#98c379;">"*"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">a </span><span style="color:#d19a66;">href</span><span>=</span><span style="color:#98c379;">"/page1"</span><span>&gt;Go To Page 1&lt;/</span><span style="color:#e06c75;">a</span><span>&gt; </span><span style="font-style:italic;color:#848da1;">&lt;!-- boosted with the attribute settings above --&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">a </span><span style="color:#d19a66;">href</span><span>=</span><span style="color:#98c379;">"/page2" </span><span style="color:#d19a66;">hx-boost</span><span>=</span><span style="color:#98c379;">"unset"</span><span>&gt;Go To Page 1&lt;/</span><span style="color:#e06c75;">a</span><span>&gt; </span><span style="font-style:italic;color:#848da1;">&lt;!-- not boosted --&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/test" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"this"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">button</span><span>&gt; </span><span style="font-style:italic;color:#848da1;">&lt;!-- hx-select is not inherited --&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-boost</span><span>=</span><span style="color:#98c379;">"true" </span><span style="color:#d19a66;">hx-select</span><span>=</span><span style="color:#98c379;">"#content" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#content" </span><span style="color:#d19a66;">hx-disinherit</span><span>=</span><span style="color:#98c379;">"hx-target"</span><span>&gt;
</span><span>  </span><span style="font-style:italic;color:#848da1;">&lt;!-- hx-select is automatically set to parent's value; hx-target is not inherited --&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/test"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-select</span><span>=</span><span style="color:#98c379;">"#content"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-boost</span><span>=</span><span style="color:#98c379;">"true" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#content" </span><span style="color:#d19a66;">hx-disinherit</span><span>=</span><span style="color:#98c379;">"hx-select"</span><span>&gt;
</span><span>    </span><span style="font-style:italic;color:#848da1;">&lt;!-- hx-target is automatically inherited from parent's value --&gt;
</span><span>    </span><span style="font-style:italic;color:#848da1;">&lt;!-- hx-select is not inherited, because the direct parent does
</span><span style="font-style:italic;color:#848da1;">    disables inheritance, despite not specifying hx-select itself --&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/test"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h2 id="notes">Notes</h2>- Read more about <a href="https://htmx.org/docs/#inheritance">Attribute Inheritance</a>

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-disabled-elt

URL: https://htmx.org/attributes/hx-disabled-elt/

<h1><code>hx-disabled-elt</code></h1>The <code>hx-disabled-elt</code> attribute allows you to specify elements that will have the <code>disabled</code> attribute
added to them for the duration of the request. The value of this attribute can be:

- A CSS query selector of the element to disable.
- <code>this</code> to disable the element itself
- <code>closest &lt;CSS selector&gt;</code> which will find the <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Element/closest">closest</a>
ancestor element or itself, that matches the given CSS selector
(e.g. <code>closest fieldset</code> will disable the closest to the element <code>fieldset</code>).
- <code>find &lt;CSS selector&gt;</code> which will find the first child descendant element that matches the given CSS selector
- <code>next</code> which resolves to <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Element/nextElementSibling">element.nextElementSibling</a>
- <code>next &lt;CSS selector&gt;</code> which will scan the DOM forward for the first element that matches the given CSS selector
(e.g. <code>next button</code> will disable the closest following sibling <code>button</code> element)
- <code>previous</code> which resolves to <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Element/previousElementSibling">element.previousElementSibling</a>
- <code>previous &lt;CSS selector&gt;</code> which will scan the DOM backwards for the first element that matches the given CSS selector.
(e.g <code>previous input</code> will disable the closest previous sibling <code>input</code> element)

Here is an example with a button that will disable itself during a request:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-disabled-elt</span><span>=</span><span style="color:#98c379;">"this"</span><span>&gt;
</span><span>    Post It!
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>When a request is in flight, this will cause the button to be marked with <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/disabled">the <code>disabled</code> attribute</a>,
which will prevent further clicks from occurring.

The <code>hx-disabled-elt</code> attribute also supports specifying multiple CSS selectors separated by commas to disable multiple elements during the request. Here is an example that disables buttons and text input fields of a particular form during the request:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-disabled-elt</span><span>=</span><span style="color:#98c379;">"find input[type='text'], find button"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text" </span><span style="color:#d19a66;">placeholder</span><span>=</span><span style="color:#98c379;">"Type here..."</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"submit"</span><span>&gt;Send&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre><h2 id="notes">Notes</h2>- <code>hx-disabled-elt</code> is inherited and can be placed on a parent element

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-delete

URL: https://htmx.org/attributes/hx-delete/

<h1><code>hx-delete</code></h1>The <code>hx-delete</code> attribute will cause an element to issue a <code>DELETE</code> to the specified URL and swap
the HTML into the DOM using a swap strategy:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-delete</span><span>=</span><span style="color:#98c379;">"/account" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"body"</span><span>&gt;
</span><span>  Delete Your Account
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre>This example will cause the <code>button</code> to issue a <code>DELETE</code> to <code>/account</code> and swap the returned HTML into
the <code>innerHTML</code> of the <code>body</code>.

<h2 id="notes">Notes</h2>- <code>hx-delete</code> is not inherited
- You can control the target of the swap using the <a href="https://htmx.org/attributes/hx-target/">hx-target</a> attribute
- You can control the swap strategy by using the <a href="https://htmx.org/attributes/hx-swap/">hx-swap</a> attribute
- You can control what event triggers the request with the <a href="https://htmx.org/attributes/hx-trigger/">hx-trigger</a> attribute
- You can control the data submitted with the request in various ways, documented here: <a href="https://htmx.org/docs/#parameters">Parameters</a>
- To remove the element following a successful <code>DELETE</code>, return a <code>200</code> status code with an empty body; if the server responds with a <code>204</code>, no swap takes place, documented here: <a href="https://htmx.org/docs/#requests">Requests &amp; Responses</a>

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-confirm

URL: https://htmx.org/attributes/hx-confirm/

<h1><code>hx-confirm</code></h1>The <code>hx-confirm</code> attribute allows you to confirm an action before issuing a request.  This can be useful
in cases where the action is destructive and you want to ensure that the user really wants to do it.

Here is an example:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-delete</span><span>=</span><span style="color:#98c379;">"/account" </span><span style="color:#d19a66;">hx-confirm</span><span>=</span><span style="color:#98c379;">"Are you sure you wish to delete your account?"</span><span>&gt;
</span><span>  Delete My Account
</span><span>&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span></code></pre><h2 id="event-details">Event details</h2>The event triggered by <code>hx-confirm</code> contains additional properties in its <code>detail</code>:

- triggeringEvent: the event that triggered the original request
- issueRequest(skipConfirmation=false): a callback which can be used to confirm the AJAX request
- question: the value of the <code>hx-confirm</code> attribute on the HTML element

<h2 id="notes">Notes</h2>- <code>hx-confirm</code> is inherited and can be placed on a parent element
- <code>hx-confirm</code> uses the browser’s <code>window.confirm</code> by default. You can customize this behavior as shown <a href="https://htmx.org/examples/confirm/">in this example</a>.
- a boolean <code>skipConfirmation</code> can be passed to the <code>issueRequest</code> callback; if true (defaults to false), the <code>window.confirm</code> will not be called and the AJAX request is issued directly

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-boost

URL: https://htmx.org/attributes/hx-boost/

<h1><code>hx-boost</code></h1>The <code>hx-boost</code> attribute allows you to “boost” normal anchors and form tags to use AJAX instead.  This
has the <a rel="noopener" target="_blank" href="https://en.wikipedia.org/wiki/Progressive_enhancement">nice fallback</a> that, if the user does not
have javascript enabled, the site will continue to work.

For anchor tags, clicking on the anchor will issue a <code>GET</code> request to the url specified in the <code>href</code> and
will push the url so that a history entry is created.  The target is the <code>&lt;body&gt;</code> tag, and the <code>innerHTML</code>
swap strategy is used by default.  All of these can be modified by using the appropriate attributes, except
the <code>click</code> trigger.

For forms the request will be converted into a <code>GET</code> or <code>POST</code>, based on the method in the <code>method</code> attribute
and will be triggered by a <code>submit</code>.  Again, the target will be the <code>body</code> of the page, and the <code>innerHTML</code>
swap will be used. The url will <em>not</em> be pushed, however, and no history entry will be created. (You can use the
<a href="https://htmx.org/attributes/hx-push-url/">hx-push-url</a> attribute if you want the url to be pushed.)

Here is an example of some boosted links:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-boost</span><span>=</span><span style="color:#98c379;">"true"</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">a </span><span style="color:#d19a66;">href</span><span>=</span><span style="color:#98c379;">"/page1"</span><span>&gt;Go To Page 1&lt;/</span><span style="color:#e06c75;">a</span><span>&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">a </span><span style="color:#d19a66;">href</span><span>=</span><span style="color:#98c379;">"/page2"</span><span>&gt;Go To Page 2&lt;/</span><span style="color:#e06c75;">a</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>These links will issue an ajax <code>GET</code> request to the respective URLs and replace the body’s inner content with it.

Here is an example of a boosted form:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">hx-boost</span><span>=</span><span style="color:#98c379;">"true" </span><span style="color:#d19a66;">action</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">method</span><span>=</span><span style="color:#98c379;">"post"</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"email" </span><span style="color:#d19a66;">placeholder</span><span>=</span><span style="color:#98c379;">"Enter email..."</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button</span><span>&gt;Submit&lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre>This form will issue an ajax <code>POST</code> to the given URL and replace the body’s inner content with it.

<h2 id="notes">Notes</h2>- <code>hx-boost</code> is inherited and can be placed on a parent element
- Only links that are to the same domain and that are not local anchors will be boosted
- All requests are done via AJAX, so keep that in mind when doing things like redirects
- To find out if the request results from a boosted anchor or form, look for <a href="https://htmx.org/reference/#request_headers"><code>HX-Boosted</code></a> in the request header
- Selectively disable boost on child elements with <code>hx-boost="false"</code>
- Disable the replacement of elements via boost, and their children, with <a href="https://htmx.org/attributes/hx-preserve/"><code>hx-preserve="true"</code></a>

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-vals

URL: https://htmx.org/attributes/hx-vals/

<h1><code>hx-vals</code></h1>The <code>hx-vals</code> attribute allows you to add to the parameters that will be submitted with an AJAX request.

By default, the value of this attribute is a list of name-expression values in <a rel="noopener" target="_blank" href="https://www.json.org/json-en.html">JSON (JavaScript Object Notation)</a>
format.

If you wish for <code>hx-vals</code> to <em>evaluate</em> the values given, you can prefix the values with <code>javascript:</code> or <code>js:</code>.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-vals</span><span>=</span><span style="color:#98c379;">'{"myVal": "My Value"}'</span><span>&gt;Get Some HTML, Including A Value in the Request&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-vals</span><span>=</span><span style="color:#98c379;">'js:{myVal: calculateValue()}'</span><span>&gt;Get Some HTML, Including a Dynamic Value from Javascript in the Request&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>When using evaluated code you can access the <code>event</code> object. This example includes the value of the last typed key within the input.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"keyup" </span><span style="color:#d19a66;">hx-vals</span><span>=</span><span style="color:#98c379;">'js:{lastKey: event.key}'</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">type</span><span>=</span><span style="color:#98c379;">"text" </span><span>/&gt;
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h2 id="security-considerations">Security Considerations</h2>- By default, the value of <code>hx-vals</code> must be valid <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Glossary/JSON">JSON</a>.
It is <strong>not</strong> dynamically computed.  If you use the <code>javascript:</code> prefix, be aware that you are introducing
security considerations, especially when dealing with user input such as query strings or user-generated content,
which could introduce a <a rel="noopener" target="_blank" href="https://owasp.org/www-community/attacks/xss/">Cross-Site Scripting (XSS)</a> vulnerability.

<h2 id="notes">Notes</h2>- <code>hx-vals</code> is inherited and can be placed on a parent element.
- A child declaration of a variable overrides a parent declaration.
- Input values with the same name will be overridden by variable declarations.

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-trigger

URL: https://htmx.org/attributes/hx-trigger/

<h1><code>hx-trigger</code></h1>The <code>hx-trigger</code> attribute allows you to specify what triggers an AJAX request.  A trigger
value can be one of the following:

- An event name (e.g. “click” or “my-custom-event”) followed by an event filter and a set of event modifiers
- A polling definition of the form <code>every &lt;timing declaration&gt;</code>
- A comma-separated list of such events

### Standard EventsA standard event, such as <code>click</code> can be specified as the trigger like so:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/clicked" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"click"</span><span>&gt;Click Me&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><h4 id="standard-event-filters">Standard Event Filters</h4>Events can be filtered by enclosing a boolean javascript expression in square brackets after the event name.  If
this expression evaluates to <code>true</code> the event will be triggered, otherwise it will be ignored.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/clicked" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"click[ctrlKey]"</span><span>&gt;Control Click Me&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This event will trigger if a click event is triggered with the <code>event.ctrlKey</code> property set to true.

Conditions can also refer to global functions or state

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/clicked" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"click[checkGlobalState()]"</span><span>&gt;Control Click Me&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>And can also be combined using the standard javascript syntax

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/clicked" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"click[ctrlKey&amp;&amp;shiftKey]"</span><span>&gt;Control-Shift Click Me&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>Note that all symbols used in the expression will be resolved first against the triggering event, and then next
against the global namespace, so <code>myEvent[foo]</code> will first look for a property named <code>foo</code> on the event, then look
for a global symbol with the name <code>foo</code>

<h4 id="standard-event-modifiers">Standard Event Modifiers</h4>Standard events can also have modifiers that change how they behave.  The modifiers are:

- <code>once</code> - the event will only trigger once (e.g. the first click)
- <code>changed</code> - the event will only change if the value of the element has changed. Please pay attention <code>change</code> is the name of the event and <code>changed</code> is the name of the modifier.
- <code>delay:&lt;timing declaration&gt;</code> - a delay will occur before an event triggers a request.  If the event
is seen again it will reset the delay.
- <code>throttle:&lt;timing declaration&gt;</code> - a throttle will occur after an event triggers a request. If the event
is seen again before the delay completes, it is ignored, the element will trigger at the end of the delay.
- <code>from:&lt;Extended CSS selector&gt;</code> - allows the event that triggers a request to come from another element in the document (e.g. listening to a key event on the body, to support hot keys)
<ul>
<li>A standard CSS selector resolves to all elements matching that selector. Thus, <code>from:input</code> would listen on every input on the page.
- The CSS selector is only evaluated once and is not re-evaluated when the page changes. If you need to detect dynamically added elements use an event filter, for example <code>click[event.target.matches('input')]</code>
- The extended CSS selector here allows for the following non-standard CSS values:
<ul>
<li><code>document</code> - listen for events on the document
- <code>window</code> - listen for events on the window
- <code>closest &lt;CSS selector&gt;</code> - finds the <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Element/closest">closest</a> ancestor element or itself, matching the given css selector
- <code>find &lt;CSS selector&gt;</code> - finds the closest child matching the given css selector
- <code>next</code> resolves to <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Element/nextElementSibling">element.nextElementSibling</a>
- <code>next &lt;CSS selector&gt;</code> scans the DOM forward for the first element that matches the given CSS selector.
(e.g. <code>next .error</code> will target the closest following sibling element with <code>error</code> class)
- <code>previous</code> resolves to <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Element/previousElementSibling">element.previousElementSibling</a>
- <code>previous &lt;CSS selector&gt;</code> scans the DOM backwards for the first element that matches the given CSS selector.
(e.g <code>previous .error</code> will target the closest previous sibling with <code>error</code> class)


</li>
</ul>
</li>
<li><code>target:&lt;CSS selector&gt;</code> - allows you to filter via a CSS selector on the target of the event.  This can be useful when you want to listen for
triggers from elements that might not be in the DOM at the point of initialization, by, for example, listening on the body,
but with a target filter for a child element</li>
<li><code>consume</code> - if this option is included the event will not trigger any other htmx requests on parents (or on elements
listening on parents)</li>
<li><code>queue:&lt;queue option&gt;</code> - determines how events are queued if an event occurs while a request for another event is in flight.  Options are:
- <code>first</code> - queue the first event
- <code>last</code> - queue the last event (default)
- <code>all</code> - queue all events (issue a request for each event)
- <code>none</code> - do not queue new events


</li>
</ul>Here is an example of a search box that searches on <code>keyup</code>, but only if the search value has changed
and the user hasn’t typed anything new for 1 second:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">name</span><span>=</span><span style="color:#98c379;">"q"
</span><span>       </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/search" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"keyup changed delay:1s"
</span><span>       </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#search-results"</span><span>/&gt;
</span></code></pre>The response from the <code>/search</code> url will be appended to the <code>div</code> with the id <code>search-results</code>.

### Non-standard EventsThere are some additional non-standard events that htmx supports:

- <code>load</code> - triggered on load (useful for lazy-loading something)
- <code>revealed</code> - triggered when an element is scrolled into the viewport (also useful for lazy-loading). If you are using <code>overflow</code> in css like <code>overflow-y: scroll</code> you should use <code>intersect once</code> instead of <code>revealed</code>.
- <code>intersect</code> - fires once when an element first intersects the viewport.  This supports two additional options:
<ul>
<li><code>root:&lt;selector&gt;</code> - a CSS selector of the root element for intersection
- <code>threshold:&lt;float&gt;</code> - a floating point number between 0.0 and 1.0, indicating what amount of intersection to fire the event on


</li>
</ul>### Triggering via the <code>HX-Trigger</code> headerIf you’re trying to fire an event from <code>HX-Trigger</code> response  header, you will likely want to
use the <code>from:body</code> modifier.  E.g. if you send a header like this <code>HX-Trigger: my-custom-event</code>
with a response, an element would likely need to look like this:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"my-custom-event from:body"</span><span>&gt;
</span><span>    Triggered by HX-Trigger header...
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>in order to fire.

This is because the header will likely trigger the event in a different DOM hierarchy than the element that you
wish to be triggered.  For a similar reason, you will often listen for hot keys from the body.

### PollingBy using the syntax <code>every &lt;timing declaration&gt;</code> you can have an element poll periodically:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/latest_updates" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"every 1s"</span><span>&gt;
</span><span>  Nothing Yet!
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This example will issue a <code>GET</code> to the <code>/latest_updates</code> URL every second and swap the results into
the innerHTML of this div.

If you want to add a filter to polling, it should be added <em>after</em> the poll declaration:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/latest_updates" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"every 1s [someConditional]"</span><span>&gt;
</span><span>  Nothing Yet!
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>### Multiple TriggersMultiple triggers can be provided, separated by commas.  Each trigger gets its own options.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/news" </span><span style="color:#d19a66;">hx-trigger</span><span>=</span><span style="color:#98c379;">"load, click delay:1s"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>This example will load <code>/news</code> immediately on page load, and then again with a delay of one second after each click.

### Via JavaScriptThe AJAX request can be triggered via JavaScript <a href="https://htmx.org/api/#trigger"><code>htmx.trigger()</code></a>, too.

<h2 id="notes">Notes</h2>- <code>hx-trigger</code> is not inherited
- <code>hx-trigger</code> can be used without an AJAX request, in which case it will only fire the <code>htmx:trigger</code> event
- In order to pass a CSS selector that contains whitespace (e.g. <code>form input</code>) to the <code>from</code>- or <code>target</code>-modifier, surround the selector in parentheses or curly brackets (e.g. <code>from:(form input)</code> or <code>from:nearest (form input)</code>)

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-target

URL: https://htmx.org/attributes/hx-target/

<h1><code>hx-target</code></h1>The <code>hx-target</code> attribute allows you to target a different element for swapping than the one issuing the AJAX
request.  The value of this attribute can be:

- A CSS query selector of the element to target.
- <code>this</code> which indicates that the element that the <code>hx-target</code> attribute is on is the target.
- <code>closest &lt;CSS selector&gt;</code> which will find the <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Element/closest">closest</a>
ancestor element or itself, that matches the given CSS selector
(e.g. <code>closest tr</code> will target the closest table row to the element).
- <code>find &lt;CSS selector&gt;</code> which will find the first child descendant element that matches the given CSS selector.
- <code>next</code> which resolves to <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Element/nextElementSibling">element.nextElementSibling</a>
- <code>next &lt;CSS selector&gt;</code> which will scan the DOM forward for the first element that matches the given CSS selector.
(e.g. <code>next .error</code> will target the closest following sibling element with <code>error</code> class)
- <code>previous</code> which resolves to <a rel="noopener" target="_blank" href="https://developer.mozilla.org/docs/Web/API/Element/previousElementSibling">element.previousElementSibling</a>
- <code>previous &lt;CSS selector&gt;</code> which will scan the DOM backwards for the first element that matches the given CSS selector.
(e.g <code>previous .error</code> will target the closest previous sibling with <code>error</code> class)

Here is an example that targets a div:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"response-div"</span><span>&gt;&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">button </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/register" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#response-div" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"beforeend"</span><span>&gt;
</span><span>        Register!
</span><span>    &lt;/</span><span style="color:#e06c75;">button</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>The response from the <code>/register</code> url will be appended to the <code>div</code> with the id <code>response-div</code>.

This example uses <code>hx-target="this"</code> to make a link that updates itself when clicked:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">a </span><span style="color:#d19a66;">hx-post</span><span>=</span><span style="color:#98c379;">"/new-link" </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"this" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML"</span><span>&gt;New link&lt;/</span><span style="color:#e06c75;">a</span><span>&gt;
</span></code></pre><h2 id="notes">Notes</h2>- <code>hx-target</code> is inherited and can be placed on a parent element

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-swap

URL: https://htmx.org/attributes/hx-swap/

<h1><code>hx-swap</code></h1>The <code>hx-swap</code> attribute allows you to specify how the response will be swapped in relative to the
<a href="https://htmx.org/attributes/hx-target/">target</a> of an AJAX request. If you do not specify the option, the default is
<code>htmx.config.defaultSwapStyle</code> (<code>innerHTML</code>).

The possible values of this attribute are:

- <code>innerHTML</code> - Replace the inner html of the target element
- <code>outerHTML</code> - Replace the entire target element with the response
- <code>textContent</code> - Replace the text content of the target element, without parsing the response as HTML
- <code>beforebegin</code> - Insert the response before the target element
- <code>afterbegin</code> - Insert the response before the first child of the target element
- <code>beforeend</code> - Insert the response after the last child of the target element
- <code>afterend</code> - Insert the response after the target element
- <code>delete</code> - Deletes the target element regardless of the response
- <code>none</code>- Does not append content from response (out of band items will still be processed).

These options are based on standard DOM naming and the
<a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentHTML"><code>Element.insertAdjacentHTML</code></a>
specification.

So in this code:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"afterend"</span><span>&gt;Get Some HTML &amp; Append It&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>The <code>div</code> will issue a request to <code>/example</code> and append the returned content after the <code>div</code>

### ModifiersThe <code>hx-swap</code> attributes supports modifiers for changing the behavior of the swap.  They are outlined below.

<h4 id="transition-transition">Transition: <code>transition</code></h4>If you want to use the new <a rel="noopener" target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API">View Transitions</a> API
when a swap occurs, you can use the <code>transition:true</code> option for your swap.  You can also enable this feature globally by
setting the <code>htmx.config.globalViewTransitions</code> config setting to <code>true</code>.

<h4 id="timing-swap-settle">Timing: <code>swap</code> &amp; <code>settle</code></h4>You can modify the amount of time that htmx will wait after receiving a response to swap the content
by including a <code>swap</code> modifier:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  </span><span style="font-style:italic;color:#848da1;">&lt;!-- this will wait 1s before doing the swap after it is received --&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"innerHTML swap:1s"</span><span>&gt;Get Some HTML &amp; Append It&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>Similarly, you can modify the time between the swap and the settle logic by including a <code>settle</code>
modifier:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  </span><span style="font-style:italic;color:#848da1;">&lt;!-- this will wait 1s before doing the swap after it is received --&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"innerHTML settle:1s"</span><span>&gt;Get Some HTML &amp; Append It&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>These attributes can be used to synchronize htmx with the timing of CSS transition effects.

<h4 id="title-ignoretitle">Title: <code>ignoreTitle</code></h4>By default, htmx will update the title of the page if it finds a <code>&lt;title&gt;</code> tag in the response content.  You can turn
off this behavior by setting the <code>ignoreTitle</code> option to true.

<h4 id="scrolling-scroll-show">Scrolling: <code>scroll</code> &amp; <code>show</code></h4>You can also change the scrolling behavior of the target element by using the <code>scroll</code> and <code>show</code> modifiers, both
of which take the values <code>top</code> and <code>bottom</code>:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  </span><span style="font-style:italic;color:#848da1;">&lt;!-- this fixed-height div will scroll to the bottom of the div after content is appended --&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">style</span><span>=</span><span style="color:#98c379;">"</span><span>height:</span><span style="color:#d19a66;">200px</span><span>; overflow: scroll</span><span style="color:#98c379;">" 
</span><span>       </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" 
</span><span>       </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"beforeend scroll:bottom"</span><span>&gt;
</span><span>     Get Some HTML &amp; Append It &amp; Scroll To Bottom
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre><pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  </span><span style="font-style:italic;color:#848da1;">&lt;!-- this will get some content and add it to #another-div, then ensure that the top of #another-div is visible in the 
</span><span style="font-style:italic;color:#848da1;">       viewport --&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" 
</span><span>       </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"innerHTML show:top"
</span><span>       </span><span style="color:#d19a66;">hx-target</span><span>=</span><span style="color:#98c379;">"#another-div"</span><span>&gt;
</span><span>    Get Some Content
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>If you wish to target a different element for scrolling or showing, you may place a CSS selector after the <code>scroll:</code>
or <code>show:</code>, followed by <code>:top</code> or <code>:bottom</code>:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  </span><span style="font-style:italic;color:#848da1;">&lt;!-- this will get some content and swap it into the current div, then ensure that the top of #another-div is visible in the 
</span><span style="font-style:italic;color:#848da1;">       viewport --&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" 
</span><span>       </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"innerHTML show:#another-div:top"</span><span>&gt;
</span><span>    Get Some Content
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>You may also use <code>window:top</code> and <code>window:bottom</code> to scroll to the top and bottom of the current window.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  </span><span style="font-style:italic;color:#848da1;">&lt;!-- this will get some content and swap it into the current div, then ensure that the viewport is scrolled to the
</span><span style="font-style:italic;color:#848da1;">       very top --&gt;
</span><span>  &lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/example" 
</span><span>       </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"innerHTML show:window:top"</span><span>&gt;
</span><span>    Get Some Content
</span><span>  &lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span></code></pre>For boosted links and forms the default behaviour is <code>show:top</code>. You can disable it globally with
<a href="https://htmx.org/api/#config">htmx.config.scrollIntoViewOnBoost</a> or you can use <code>hx-swap="show:none"</code> on an element basis.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">form </span><span style="color:#d19a66;">action</span><span>=</span><span style="color:#98c379;">"/example" </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"show:none"</span><span>&gt;
</span><span>  ...
</span><span>&lt;/</span><span style="color:#e06c75;">form</span><span>&gt;
</span></code></pre><h4 id="focus-scroll">Focus scroll</h4>htmx preserves focus between requests for inputs that have a defined id attribute. By default htmx prevents auto-scrolling to focused inputs between requests which can be unwanted behavior on longer requests when the user has already scrolled away. To enable focus scroll you can use <code>focus-scroll:true</code>.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"name" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/validation" 
</span><span>       </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML focus-scroll:true"</span><span>/&gt;
</span></code></pre>Alternatively, if you want the page to automatically scroll to the focused element after each request you can change the htmx global configuration value <code>htmx.config.defaultFocusScroll</code> to true. Then disable it for specific requests using <code>focus-scroll:false</code>.

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>  &lt;</span><span style="color:#e06c75;">input </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"name" </span><span style="color:#d19a66;">hx-get</span><span>=</span><span style="color:#98c379;">"/validation" 
</span><span>       </span><span style="color:#d19a66;">hx-swap</span><span>=</span><span style="color:#98c379;">"outerHTML focus-scroll:false"</span><span>/&gt;
</span></code></pre><h2 id="notes">Notes</h2>- <code>hx-swap</code> is inherited and can be placed on a parent element
- The default value of this attribute is <code>innerHTML</code>
- Due to DOM limitations, it’s not possible to use the <code>outerHTML</code> method on the <code>&lt;body&gt;</code> element.
htmx will change <code>outerHTML</code> on <code>&lt;body&gt;</code> to use <code>innerHTML</code>.
- The default swap delay is 0ms
- The default settle delay is 20ms

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

# hx-swap-oob

URL: https://htmx.org/attributes/hx-swap-oob/

<h1><code>hx-swap-oob</code></h1>The <code>hx-swap-oob</code> attribute allows you to specify that some content in a response should be
swapped into the DOM somewhere other than the target, that is “Out of Band”.  This allows you to piggy back updates to other element updates on a response.

Consider the following response HTML:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span> ...
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">div </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"alerts" </span><span style="color:#d19a66;">hx-swap-oob</span><span>=</span><span style="color:#98c379;">"true"</span><span>&gt;
</span><span>    Saved!
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>
</span></code></pre>The first div will be swapped into the target the usual manner.  The second div, however, will be swapped in as a replacement for the element with the id <code>alerts</code>, and will not end up in the target.

The value of the <code>hx-swap-oob</code> can be:

- <code>true</code>
- any valid <a href="https://htmx.org/attributes/hx-swap/"><code>hx-swap</code></a> value
- any valid <a href="https://htmx.org/attributes/hx-swap/"><code>hx-swap</code></a> value, followed by a colon, followed by a CSS selector

If the value is <code>true</code> or <code>outerHTML</code> (which are equivalent) the element will be swapped inline.

If a swap value is given, that swap strategy will be used.

If a selector is given, all elements matched by that selector will be swapped.  If not, the element with an ID matching the new content will be swapped.

### Troublesome TablesNote that you can use a <code>template</code> tag to encapsulate types of elements that, by the HTML spec, can’t stand on their own in the
DOM (<code>&lt;tr&gt;</code>, <code>&lt;td&gt;</code>, <code>&lt;th&gt;</code>, <code>&lt;thead&gt;</code>, <code>&lt;tbody&gt;</code>, <code>&lt;tfoot&gt;</code>, <code>&lt;colgroup&gt;</code>, <code>&lt;caption&gt;</code> &amp; <code>&lt;col&gt;</code>).

Here is an example with an out of band swap of a table row being encapsulated in this way:

<pre data-lang="html" style="background-color:#1f2329;color:#abb2bf;" class="language-html "><code class="language-html" data-lang="html"><span>&lt;</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>    ...
</span><span>&lt;/</span><span style="color:#e06c75;">div</span><span>&gt;
</span><span>&lt;</span><span style="color:#e06c75;">template</span><span>&gt;
</span><span>    &lt;</span><span style="color:#e06c75;">tr </span><span style="color:#d19a66;">id</span><span>=</span><span style="color:#98c379;">"row" </span><span style="color:#d19a66;">hx-swap-oob</span><span>=</span><span style="color:#98c379;">"true"</span><span>&gt;
</span><span>        ...
</span><span>    &lt;/</span><span style="color:#e06c75;">tr</span><span>&gt;
</span><span>&lt;/</span><span style="color:#e06c75;">template</span><span>&gt;
</span></code></pre>Note that these template tags will be removed from the final content of the page.

<h2 id="nested-oob-swaps">Nested OOB Swaps</h2>By default, any element with <code>hx-swap-oob=</code> attribute anywhere in the response is processed for oob swap behavior, including when an element is nested within the main response element.
This can be problematic when using <a rel="noopener" target="_blank" href="https://htmx.org/essays/template-fragments/">template fragments</a> where a fragment may be reused as a oob-swap target and also as part of a bigger fragment. When the bigger fragment is the main response the inner fragment will still be processed as an oob swap, removing it from the dom.

This behavior can be changed by setting the config <code>htmx.config.allowNestedOobSwaps</code> to <code>false</code>. If this config option is <code>false</code>, OOB swaps are only processed when the element is <em>adjacent to</em> the main response element, OOB swaps elsewhere will be ignored and oob-swap-related attributes stripped.

<h2 id="notes">Notes</h2>- <code>hx-swap-oob</code> is not inherited

<div class="row" style="text-align: center;">
            <div class="col">
                <img src="/img/bss_bars.png" alt="" style="max-width: 30px; margin-top: 3em;">
            </div>
        </div>

---

