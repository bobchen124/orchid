/*pub-1|2012-05-03 16:54:08*/
(function() {
	var C = KISSY, E = C.DOM, B = C.Event;
	if (C.UA.ie) {
		var A = ["header", "article", "section", "aside","nav"];
		C.each(A, function(G) {
			document.createElement(G);
		});
	}
	
	C.namespace("MTB", true);
	MTB = {
		_version : "3.0",
		_description : "MyUub Namespace"
	};
	var F = {
		_description : "MyUub Base Module",
		selectSideMenuItem : function(I) {
			var G, H;
			G = E.get("#" + I);
			if (!G) {
				return
			}
			if (G.nodeName.toUpperCase() !== "A") {
				G = E.get("A", G);
			}
			E.addClass(G, "selected");
			H = E.parent(G, ".J_MtSideTree");
			if (!H) {
				return;
			}
			E.replaceClass(H, "fold", "unfold");
		},
		
		init : function() {
			var G = this;
			window.selectItem = G.selectSideMenuItem;
			C.available("#J_MtNotice", function() {
				//G._initNotice()
			});
			
			C.ready(function() {
				var H = E.query("LI", E.get("#J_MtMainNav"));
				G.fixHover(H, "hover");
				G._initNavMenu();
				G._initMenu();
			});
		},
		fixHover : function(G, H) {
			if (!G || !C.UA.ie) {
				return
			}
			C.each(G, function(I) {
				B.on(I, "mouseenter", function() {
					E.addClass(I, H);
				});
				B.on(I, "mouseleave", function() {
					E.removeClass(I, H);
				});
			});
		},
		_initNavMenu : function() {
			var K = E.get("#J_MtMainNav"), J = E.query(".J_MtNavSubTrigger", K), H = E
					.query(".J_MtNavSub", K), N = null, M = "hide", I = "hover", L = 200;
			if (C.UA.ie) {
				C.each(J, function(O) {
					var P = E.parent(O, "LI");
					B.on([ O, P ], "mouseenter", function() {
						E.addClass(this, I);
					});
					B.on([ O, P ], "mouseleave", function() {
						E.removeClass(this, I);
					});
				});
			}
			function G() {
				N && N.cancel && N.cancel();
			}
			B.on(J, "mouseenter", function(P) {
				var O = E.siblings(P.target, ".J_MtNavSub");
				G();
				E.removeClass(O, M);
			});
			B.on(J, "mouseleave", function(P) {
				var O = E.siblings(P.target, ".J_MtNavSub");
				N = C.later(function() {
					E.addClass(O, M);
				}, L);
			});
			B.on(H, "mouseenter", G);
			B.on(H, "mouseleave", function() {
				var O = this;
				N = C.later(function() {
					E.addClass(O, M);
				}, L);
			});
		},
		
		_initMenu : function() {
			var G = E.query(".J_MtIndicator"), I = "fold", H = "un" + I;
			B.on(G, "click", function(L) {
				L.preventDefault();
				var K = L.target, J = E.parent(K, "DD");
				E.hasClass(J, I) ? E.replaceClass(J, I, H) : E.replaceClass(J,
						H, I);
			});
		}
	};
	MTB.mtBase = F;
	F.init();
})();