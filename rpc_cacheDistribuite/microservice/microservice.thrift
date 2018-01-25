/**
 * This Thrift file can be included by other Thrift files that want to share
 * these definitions.
 */

namespace cpp microservice
namespace d microservice // "shared" would collide with the eponymous D keyword.
namespace java microservice

struct KVNews{

  1: string title,
  2: string url,

}

struct kVCollection{

  1:list<KVNews> elements

}

service Toptennews {

  void ping(),
  list<KVNews> getnewsmysql(),

}
